#!/usr/bin/env python3
"""recipe_view: render recipe JSON the way the Workato recipe editor shows it, for human review.

Produces a readable flow (trigger, numbered steps, IF/ELSE, Monitor/On error, Repeat, Stop) with
app names and operation titles from the live catalog, datapills as chips ("Email · step 2"),
formulas marked ƒ, and each step's configured fields with catalog labels.

  python3 tools/recipe_view.py md   <recipe.json>           # text view (for design.md / chat)
  python3 tools/recipe_view.py html <recipe.json> [--out f]  # HTML fragment (used by review_page.py)

Library use: render_html(doc) -> str, render_md(doc) -> str.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import recipe_check as rc  # noqa: E402

CATALOG = rc.Catalog(rc.CATALOG_DIR)
OPERAND_WORDS = {
    "equals_to": "equals", "not_equals_to": "does not equal", "contains": "contains",
    "not_contains": "does not contain", "starts_with": "starts with", "ends_with": "ends with",
    "greater_than": "is greater than", "less_than": "is less than", "present": "is present",
    "blank": "is not present", "is_true": "is true", "is_not_true": "is not true",
    "is_false": "is false", "is_not_false": "is not false",
}
KEYWORD_LABEL = {"trigger": "Trigger", "action": "Action", "if": "If", "elsif": "Else if", "else": "Else",
                 "try": "Monitor", "catch": "On error", "foreach": "Repeat for each", "repeat": "Repeat",
                 "while_condition": "While", "stop": "Stop job", "filter": "Filter"}
PILL_ANY = re.compile(r"#\{_dp\('(\{.*?\})'\)\}|_dp\('(\{.*?\})'\)|#\{_\('data\.([A-Za-z0-9_]+)\.([A-Za-z0-9_\-]+)((?:\.[^']*)?)'(?:\s*,\s*'[^']*')*\)\}|_\('data\.([A-Za-z0-9_]+)\.([A-Za-z0-9_\-]+)((?:\.[^']*)?)'(?:\s*,\s*'[^']*')*\)", re.S)
SKIP_INPUT_KEYS = {"user_logs_enabled"}


# --------------------------------------------------------------------------- catalog helpers
def app_title(provider: str | None) -> str:
    if not provider:
        return ""
    c = CATALOG.get(provider)
    if c:
        return c["title"]
    return re.sub(r"_connector_\d+_\d+$", "", provider).replace("_", " ").title() + " (custom)"


def op_info(provider: str | None, name: str | None, keyword: str) -> dict | None:
    c = CATALOG.get(provider) if provider else None
    if not c:
        return None
    for o in c["triggers" if keyword == "trigger" else "actions"]:
        if o["name"] == name:
            return o
    return None


def op_title(provider, name, keyword) -> str:
    o = op_info(provider, name, keyword)
    if o and o.get("title"):
        return o["title"]
    return (name or "").replace("__adhoc_http_action", "Custom action (HTTP)").replace("_", " ").capitalize()


def field_label(op: dict | None, key: str) -> str:
    for f in (op or {}).get("input") or []:
        if f.get("name") == key:
            return f.get("label") or key
    return key.replace("_", " ").capitalize()


def hue(provider: str) -> int:
    return int(hashlib.md5((provider or "x").encode()).hexdigest()[:4], 16) % 360


def pretty(key: str, v):
    """Classify a field value for display: ('schema', [names]) | ('responses', [...]) | ('code', text) | ('raw', v)."""
    if isinstance(v, str):
        t = v.strip()
        if t.startswith("[") and t.endswith("]"):
            try:
                arr = json.loads(t)
                if arr and all(isinstance(x, dict) and "name" in x for x in arr):
                    return "schema", [f"{x['name']} ({x.get('type', 'string')})" for x in arr]
            except Exception:
                pass
        if key in ("code", "query", "sql") and "\n" in v:
            lines = [ln for ln in v.splitlines() if ln.strip()]
            return "code", f"{len(lines)} lines of code; starts: {lines[0].strip()[:70]}"
    if key == "responses" and isinstance(v, list):
        out = []
        for r in v:
            if isinstance(r, dict):
                names = pretty("", r.get("body_schema", ""))
                fields = ", ".join(n.split(" (")[0] for n in names[1]) if names[0] == "schema" else ""
                out.append(f"{r.get('name')} ({r.get('http_status_code')}): {fields}")
        return "schema", out
    return "raw", v


# --------------------------------------------------------------------------- model
class View:
    def __init__(self, doc: dict):
        self.doc = doc
        code = doc["code"] if "code" in doc else doc
        if isinstance(code, str):
            code = json.loads(code)
        self.code = code
        self.alias = {}

        def walk(b):
            if b.get("as") and b["as"] not in self.alias:
                self.alias[b["as"]] = b
            for c in b.get("block") or []:
                walk(c)
        walk(code)

    # ---- pills
    def pill_parts(self, line: str, provider: str, path: list) -> tuple[str, str, str]:
        b = self.alias.get(line)
        last = [p for p in path if isinstance(p, str)]
        label = " ".join((last[-1] if last else line).replace("_", " ").split())
        label = label[:1].upper() + label[1:]
        if b is None:
            where = "unknown step"
        elif b.get("keyword") == "trigger":
            where = "trigger"
        else:
            where = f"step {b.get('number')}"
        if provider == "foreach":
            where = "current item"
        if provider == "catch":
            where = "error"
        return label, where, provider or ""

    def _pills(self, text: str, fmt_chip, fmt_text):
        out, pos = [], 0
        for m in PILL_ANY.finditer(text):
            out.append(fmt_text(text[pos:m.start()]))
            js = m.group(1) or m.group(2)
            try:
                if js:
                    p = json.loads(js)
                    if p.get("pill_type", "output") != "output":
                        out.append(fmt_chip(p.get("property_name") or p.get("pill_type"), "property", "property"))
                        pos = m.end()
                        continue
                    label, where, prov = self.pill_parts(p["line"], p["provider"], p.get("path", []))
                else:
                    prov = m.group(3) or m.group(6)
                    line = m.group(4) or m.group(7)
                    rest = (m.group(5) or m.group(8) or "").strip(".").split(".")
                    label, where, prov = self.pill_parts(line, prov, rest)
                out.append(fmt_chip(label, where, prov))
            except Exception:
                out.append(fmt_text(m.group(0)))
            pos = m.end()
        out.append(fmt_text(text[pos:]))
        return "".join(out)

    def value_html(self, v) -> str:
        if isinstance(v, bool) or v is None:
            return f"<span class='lit'>{html.escape(str(v).lower())}</span>"
        if not isinstance(v, str):
            return f"<span class='lit'>{html.escape(json.dumps(v))}</span>"
        formula = v.startswith("=")
        body = v[1:] if formula else v

        def chip(label, where, prov):
            return (f"<span class='pill' style='--h:{hue(prov)}'><b>{html.escape(label)}</b>"
                    f"<i>{html.escape(where)}</i></span>")
        rendered = self._pills(body, chip, lambda t: html.escape(t))
        if formula:
            return f"<span class='formula'><em title='Formula'>ƒ</em><code>{rendered}</code></span>"
        return f"<span class='txt'>{rendered}</span>"

    def value_md(self, v) -> str:
        if not isinstance(v, str):
            return json.dumps(v)
        formula = v.startswith("=")
        body = v[1:] if formula else v
        r = self._pills(body, lambda l, w, p: f"[{l} · {w}]", lambda t: t)
        r = " ".join(r.split())
        return ("ƒ " + r) if formula else r

    def condition_text(self, cond: dict, as_html: bool) -> str:
        parts = []
        for c in (cond or {}).get("conditions") or []:
            if "conditions" in c:
                parts.append("(" + self.condition_text(c, as_html) + ")")
                continue
            lhs = self.value_html(c.get("lhs", "")) if as_html else self.value_md(c.get("lhs", ""))
            op = OPERAND_WORDS.get(c.get("operand"), c.get("operand", ""))
            rhs = c.get("rhs", "")
            rhs_s = "" if rhs in ("", None) else (" " + (self.value_html(rhs) if as_html else self.value_md(rhs)))
            parts.append(f"{lhs} <span class='op'>{html.escape(op)}</span>{rhs_s}" if as_html else f"{lhs} {op}{rhs_s}")
        joiner = (" <span class='op'>%s</span> " if as_html else " %s ") % (cond or {}).get("operand", "and").upper()
        return joiner.join(parts)

    # ---- fields
    def fields(self, b: dict) -> list[tuple[str, object]]:
        op = op_info(b.get("provider"), b.get("name"), b.get("keyword"))
        out = []
        for k, v in (b.get("input") or {}).items():
            if k in SKIP_INPUT_KEYS or v in (None, "", {}, []):
                continue
            out.append((field_label(op, k), self.clean(k, v)))
        return out

    def clean(self, k, v):
        kind, val = pretty(k, v)
        if kind == "schema":
            return {"__schema__": val}
        if kind == "code":
            return {"__code__": val}
        if isinstance(v, dict):
            return {kk: self.clean(kk, vv) for kk, vv in v.items() if vv not in (None, "", {}, [])}
        return v


# --------------------------------------------------------------------------- HTML
def render_html(doc: dict, title: str | None = None) -> str:
    vw = View(doc)
    name = title or doc.get("name") or "Recipe"

    def field_rows(items, depth=0) -> str:
        rows = []
        for label, v in items:
            if isinstance(v, dict) and "__schema__" in v:
                chips = "".join(f"<span class='fieldchip'>{html.escape(n)}</span>" for n in v["__schema__"])
                rows.append(f"<div class='frow'><dt>{html.escape(label)}</dt><dd>{chips}</dd></div>")
            elif isinstance(v, dict) and "__code__" in v:
                rows.append(f"<div class='frow'><dt>{html.escape(label)}</dt><dd><span class='codeinfo'>{html.escape(v['__code__'])}</span></dd></div>")
            elif isinstance(v, dict):
                inner = field_rows([(k.replace('_', ' ').capitalize(), x) for k, x in v.items() if x not in (None, "")], depth + 1)
                rows.append(f"<div class='frow nested'><dt>{html.escape(label)}</dt><dd><dl>{inner}</dl></dd></div>")
            else:
                rows.append(f"<div class='frow'><dt>{html.escape(label)}</dt><dd>{vw.value_html(v)}</dd></div>")
        return "".join(rows)

    def step(b: dict) -> str:
        kw = b.get("keyword")
        prov = b.get("provider")
        num = b.get("number")
        kids = [c for c in b.get("block") or [] if isinstance(c, dict)]
        badge = f"<span class='num'>{'⚡' if kw == 'trigger' else num}</span>"
        kind = KEYWORD_LABEL.get(kw, kw)
        if kw in ("trigger", "action"):
            app = app_title(prov)
            head = (f"<div class='app' style='--h:{hue(prov)}'>{html.escape(app[:1])}</div>"
                    f"<div class='what'><span class='kind'>{html.escape(kind)}</span>"
                    f"<strong>{html.escape(op_title(prov, b.get('name'), kw))}</strong>"
                    f"<span class='appname'>in {html.escape(app)}</span></div>")
            body = f"<dl>{field_rows(vw.fields(b))}</dl>" if vw.fields(b) else ""
        elif kw in ("if", "elsif", "while_condition"):
            head = (f"<div class='what'><span class='kind'>{kind}</span>"
                    f"<span class='cond'>{vw.condition_text(b.get('input') or {}, True)}</span></div>")
            body = ""
        elif kw == "foreach":
            head = (f"<div class='what'><span class='kind'>{kind}</span>"
                    f"<span class='cond'>item in {vw.value_html(b.get('source', ''))}</span></div>")
            body = ""
        elif kw == "catch":
            inp = b.get("input") or {}
            r = inp.get("max_retry_count", "0")
            head = (f"<div class='what'><span class='kind'>{kind}</span>"
                    f"<span class='cond'>retry {html.escape(str(r))} time(s) every {html.escape(str(inp.get('retry_interval', '-')))}s, then run these steps</span></div>")
            body = ""
        elif kw == "stop":
            inp = b.get("input") or {}
            err = str(inp.get("stop_with_error", "false")) == "true"
            head = (f"<div class='what'><span class='kind'>{kind}</span>"
                    f"<span class='cond'>{'with error' if err else 'without error'}"
                    f"{': ' + vw.value_html(inp.get('stop_reason')) if inp.get('stop_reason') else ''}</span></div>")
            body = ""
        else:
            head = f"<div class='what'><span class='kind'>{html.escape(kind)}</span></div>"
            body = ""
        note = f"<p class='note'>{html.escape(b['comment'])}</p>" if b.get("comment") else ""
        children = ""
        if kids:
            children = "<ol class='children'>" + "".join(step(c) for c in kids) + "</ol>"
        cls = f"step k-{kw}"
        return f"<li class='{cls}'><div class='card'>{badge}{head}</div>{note}{body}{children}</li>"

    return (f"<section class='recipe' aria-label='{html.escape(name)}'>"
            f"<header class='rhead'><span class='eyebrow'>Recipe</span><h3>{html.escape(name)}</h3>"
            + (f"<p>{html.escape(doc.get('description') or '')}</p>" if doc.get("description") else "")
            + f"</header><ol class='flow'>{step(vw.code)}</ol></section>")


# --------------------------------------------------------------------------- text
def render_md(doc: dict) -> str:
    vw = View(doc)
    lines = [f"**{doc.get('name', 'Recipe')}**", ""]

    def step(b, depth):
        ind = "    " * depth
        kw, prov = b.get("keyword"), b.get("provider")
        n = "TRIGGER" if kw == "trigger" else f"{b.get('number')}."
        if kw in ("trigger", "action"):
            lines.append(f"{ind}{n} {op_title(prov, b.get('name'), kw)} — *{app_title(prov)}*")
            def emit(label, v, pre):
                if isinstance(v, dict) and "__schema__" in v:
                    lines.append(f"{pre}- {label}: {'; '.join(v['__schema__'])}")
                elif isinstance(v, dict) and "__code__" in v:
                    lines.append(f"{pre}- {label}: {v['__code__']}")
                elif isinstance(v, dict):
                    for k, x in v.items():
                        emit(f"{label} › {k}", x, pre)
                else:
                    lines.append(f"{pre}- {label}: {vw.value_md(v)}")
            for label, v in vw.fields(b):
                emit(label, v, ind + "    ")
        elif kw in ("if", "elsif", "while_condition"):
            lines.append(f"{ind}{n} {KEYWORD_LABEL[kw].upper()} {vw.condition_text(b.get('input') or {}, False)}")
        elif kw == "foreach":
            lines.append(f"{ind}{n} REPEAT FOR EACH item in {vw.value_md(b.get('source', ''))}")
        elif kw == "catch":
            lines.append(f"{ind}{n} ON ERROR (retry {(b.get('input') or {}).get('max_retry_count', '0')}x)")
        elif kw == "stop":
            inp = b.get("input") or {}
            lines.append(f"{ind}{n} STOP JOB {'with error' if str(inp.get('stop_with_error')) == 'true' else ''} "
                         f"{vw.value_md(inp.get('stop_reason', ''))}".rstrip())
        else:
            lines.append(f"{ind}{n} {KEYWORD_LABEL.get(kw, kw).upper()}")
        if b.get("comment"):
            lines.append(f"{ind}    _{b['comment']}_")
        for c in b.get("block") or []:
            step(c, depth + 1)
    step(vw.code, 0)
    return "\n".join(lines)


def load(path: Path) -> dict:
    doc, code, config, _ = rc.load_recipe(path)
    if code is None:
        raise SystemExit(f"{path}: not a recipe")
    d = dict(doc) if isinstance(doc, dict) and doc is not code else {"name": path.stem}
    d["code"] = code
    return d


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("format", choices=["md", "html"])
    ap.add_argument("recipe")
    ap.add_argument("--out")
    a = ap.parse_args()
    d = load(Path(a.recipe))
    out = render_md(d) if a.format == "md" else render_html(d)
    if a.out:
        Path(a.out).write_text(out)
    else:
        print(out)

#!/usr/bin/env python3
"""review_page: build the human review page for an automation's approval gate.

The page is written for the requester and end users, not engineers: what it does in plain words,
who benefits, the flow drawn the way the Workato recipe editor shows it (when recipes exist),
the test cases as "given → expect", decisions needed with recommendations, and how to approve.

  python3 tools/review_page.py automation <name>        -> automations/<name>/review/index.html
  python3 tools/review_page.py recipe <file> --out f    -> standalone recipe view page
Publish the HTML with the Artifact tool (the Engagement Lead does this at each gate).
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import recipe_view as rv  # noqa: E402

GATE = {
    "draft": ("Spec approval", "Confirm what we're building: purpose, users, rules, and the test cases that prove it works."),
    "specified": ("Design approval", "Confirm how it's built: the recipe flow below is exactly what the team will build."),
    "designed": ("In build", "The team is building and checking the recipes."),
    "built": ("In validation", "QA is checking the recipes."),
    "validated": ("Ready to save", "Recipes passed checks and are about to be saved, stopped, in your workspace."),
    "pushed": ("In testing", "Recipes are saved, stopped, in your workspace; test cases are running."),
    "tested": ("Go-live approval", "All test cases passed. Approve to start the automation."),
    "deployed": ("Live", "The automation is running."),
}

CSS = r"""
<style>
/* Layout: one review column (~74ch) with a vertical recipe rail; summary first, detail after. */
:root{
  --bg:#f5f7f9; --surface:#ffffff; --ink:#152033; --muted:#5b6678; --line:#dfe4ea;
  --accent:#2d5bd2; --accent-ink:#ffffff; --ok:#1f7a4d; --warn:#9a5b00; --err:#b3261e;
  --k-if:#6b3fb6; --k-try:#9a5b00; --k-loop:#1d6fa5; --k-stop:#b3261e;
  --pill-l:93%; --pill-t:28%; --tile-l:46%;
  --display:"Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body:"Source Sans 3", "Segoe UI", system-ui, sans-serif;
  --mono:"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f141c; --surface:#161d28; --ink:#e6ebf2; --muted:#9aa6b8; --line:#2a3443;
  --accent:#7aa2ff; --accent-ink:#0f141c; --ok:#5fd39a; --warn:#f0b35a; --err:#ff8a80;
  --k-if:#c3a6ff; --k-try:#f0b35a; --k-loop:#7cc4f2; --k-stop:#ff8a80;
  --pill-l:24%; --pill-t:86%; --tile-l:58%; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f141c; --surface:#161d28; --ink:#e6ebf2; --muted:#9aa6b8; --line:#2a3443;
  --accent:#7aa2ff; --accent-ink:#0f141c; --ok:#5fd39a; --warn:#f0b35a; --err:#ff8a80;
  --k-if:#c3a6ff; --k-try:#f0b35a; --k-loop:#7cc4f2; --k-stop:#ff8a80;
  --pill-l:24%; --pill-t:86%; --tile-l:58%; color-scheme:dark}
body{background:var(--bg);color:var(--ink);font:16px/1.55 var(--body);
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}
.wrap{max-width:820px;margin:0 auto;display:grid;gap:28px}
h1,h2,h3{font-family:var(--display);text-wrap:balance;margin:0;line-height:1.15}
h1{font-size:clamp(1.7rem,4vw,2.3rem);font-weight:700;letter-spacing:-.01em}
h2{font-size:1.25rem;font-weight:650}
h3{font-size:1.05rem;font-weight:650}
p{margin:0;max-width:68ch}
.eyebrow{font:600 .72rem/1 var(--body);letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
header.top{display:grid;gap:10px}
.status{display:inline-flex;gap:8px;align-items:center;font-weight:600;font-size:.85rem;color:var(--accent);
  border:1px solid var(--accent);border-radius:999px;padding:3px 12px;width:max-content;max-width:100%}
.lede{font-size:1.08rem;color:var(--ink)}
section{display:grid;gap:14px}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px;display:grid;gap:12px}
.approve{border-color:var(--accent)}
.approve ul{margin:0;padding-left:1.2em;display:grid;gap:4px}
.copy{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.copy code{font:500 .9rem var(--mono);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px;overflow-wrap:anywhere;min-width:0}
button{font:600 .9rem var(--body);background:var(--accent);color:var(--accent-ink);border:0;border-radius:8px;padding:9px 14px;cursor:pointer}
button:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.users{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.user{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px;display:grid;gap:6px;min-width:0}
.user b{font-family:var(--display)}
.user .muted{color:var(--muted);font-size:.93rem}
ul.plain{margin:0;padding-left:1.2em;display:grid;gap:4px}
.tests{display:grid;gap:10px}
.test{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px;display:grid;grid-template-columns:auto 1fr;gap:6px 14px;min-width:0}
.test .id{font:700 .8rem var(--mono);color:var(--accent);grid-row:span 3;padding-top:2px}
.test dt{font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.test dd{margin:0;min-width:0;overflow-wrap:anywhere}
.qs{display:grid;gap:10px}
.q{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px;display:grid;gap:6px}
.q .rec{color:var(--ok);font-weight:600}
.q .rec::before{content:"Recommended: ";color:var(--muted);font-weight:500}
.q .ans{color:var(--ink);font-weight:600}
.q .ans::before{content:"Your answer: ";color:var(--muted);font-weight:500}
.kv{display:grid;grid-template-columns:minmax(120px,max-content) 1fr;gap:6px 16px}
.kv dt{color:var(--muted)} .kv dd{margin:0;min-width:0;overflow-wrap:anywhere}
/* recipe editor view */
.recipe{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px;display:grid;gap:14px;min-width:0}
.rhead{display:grid;gap:4px} .rhead p{color:var(--muted)}
ol.flow,ol.children{list-style:none;margin:0;padding:0;display:grid;gap:10px}
ol.children{margin-top:10px;margin-left:15px;padding-left:16px;border-left:2px solid var(--line)}
.step{min-width:0}
.card{display:flex;gap:12px;align-items:flex-start;min-width:0}
.num{flex:none;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;font:700 .8rem var(--mono);
  background:var(--bg);border:1px solid var(--line);color:var(--muted)}
.app{flex:none;width:30px;height:30px;border-radius:8px;display:grid;place-items:center;font:700 .9rem var(--display);
  background:hsl(var(--h) 55% var(--tile-l));color:#fff}
.what{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;min-width:0;padding-top:4px}
.kind{font:700 .7rem/1 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.k-if>.card .kind,.k-elsif>.card .kind,.k-else>.card .kind{color:var(--k-if)}
.k-try>.card .kind,.k-catch>.card .kind{color:var(--k-try)}
.k-foreach>.card .kind,.k-repeat>.card .kind,.k-while_condition>.card .kind{color:var(--k-loop)}
.k-stop>.card .kind{color:var(--k-stop)}
.appname{color:var(--muted);font-size:.9rem}
.cond{min-width:0;overflow-wrap:anywhere}
.op{font-weight:600;color:var(--k-if)}
.step dl{margin:8px 0 0 42px;display:grid;gap:6px}
.frow{display:grid;grid-template-columns:minmax(110px,max-content) 1fr;gap:4px 12px;font-size:.93rem}
.frow dt{color:var(--muted)} .frow dd{margin:0;min-width:0;overflow-wrap:anywhere}
.frow.nested dd dl{margin:0}
.note{margin:6px 0 0 42px;color:var(--muted);font-style:italic;font-size:.92rem}
.pill{display:inline-flex;gap:6px;align-items:baseline;border-radius:999px;padding:1px 9px;margin:1px 2px;
  background:hsl(var(--h) 70% var(--pill-l));color:hsl(var(--h) 45% var(--pill-t));font-size:.86rem;white-space:nowrap}
.pill i{font-style:normal;opacity:.75;font-size:.78rem}
.formula{display:inline-flex;gap:6px;align-items:baseline;min-width:0}
.formula em{font-style:normal;font-weight:700;color:var(--accent)}
.formula code{font:.86rem var(--mono);overflow-wrap:anywhere}
.fieldchip{display:inline-block;font:.8rem var(--mono);border:1px solid var(--line);border-radius:6px;padding:1px 7px;margin:2px 4px 2px 0}
.codeinfo{font-size:.88rem;color:var(--muted)}
.lit{font-family:var(--mono);font-size:.88rem}
footer{color:var(--muted);font-size:.85rem}
@media (max-width:480px){.step dl,.note{margin-left:0}.frow{grid-template-columns:1fr}.kv{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700'
         '&family=JetBrains+Mono:wght@400;500;700&family=Source+Sans+3:wght@400;500;600;700&display=swap">')

COPY_JS = """<script>
document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){
  var t=document.getElementById(b.dataset.copy);var s=t.textContent;
  function sel(){var r=document.createRange();r.selectNodeContents(t);var w=getSelection();w.removeAllRanges();w.addRange(r);}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(s).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy';},1600)},sel)}else{sel()}
});});
</script>"""


def e(x) -> str:
    return html.escape(str(x if x is not None else ""))


def head(title: str) -> str:
    return (f'<title>{e(title)}</title><meta name="claude:viewport-fit-sides" content="cover">{FONTS}{CSS}')


def automation_page(name: str) -> str:
    import yaml
    d = ROOT / "automations" / name
    spec = yaml.safe_load((d / "spec.yaml").read_text())
    st = json.loads((d / "state.json").read_text())
    stage = st["state"]
    gate_title, gate_text = GATE.get(stage, (stage, ""))
    title = spec.get("title") or name
    parts = [head(title), '<div class="wrap">']

    parts.append(f"""<header class="top"><span class="eyebrow">Workato automation · {e(name)}</span>
<h1>{e(title)}</h1><span class="status">{e(gate_title)}</span><p class="lede">{e(spec.get('summary', '').strip())}</p></header>""")

    # approval panel
    if stage in ("draft", "specified", "tested"):
        gate_key = {"draft": "spec", "specified": "design", "tested": "go-live"}[stage]
        answers = "with your recommendations" if gate_key == "spec" and spec.get("open_questions") else ""
        approve_text = f"approve {gate_key} {answers}".strip()
        checks = {
            "spec": ["The purpose and users below match what you need",
                     "Each test case shows the result you expect",
                     "The decisions below are answered (accept the recommendations or change them)"],
            "design": ["The recipe flow does what the spec says, step by step",
                       "Error handling and messages are what end users should see",
                       "Nothing is missing from the flow"],
            "go-live": ["All test cases passed (see report)", "You're ready for real use"],
        }[gate_key]
        parts.append(f"""<section class="panel approve" aria-labelledby="ap"><h2 id="ap">What you're approving</h2>
<p>{e(gate_text)}</p><ul>{''.join(f'<li>{e(c)}</li>' for c in checks)}</ul>
<p>To approve, reply in Claude with this text, or tell Claude what to change:</p>
<div class="copy"><code id="approve-text">{e(approve_text)}</code><button type="button" data-copy="approve-text">Copy</button></div></section>""")

    # users & success
    users = spec.get("end_users") or []
    if users:
        cards = "".join(f"""<div class="user"><b>{e(u.get('who'))}</b><span class="muted">Needs: {e(u.get('need'))}</span>
<span>Gets: {e(u.get('experience'))}</span></div>""" for u in users)
        parts.append(f'<section aria-labelledby="who"><h2 id="who">Who it\'s for</h2><div class="users">{cards}</div></section>')
    if spec.get("success_measures"):
        parts.append('<section aria-labelledby="sm"><h2 id="sm">How we\'ll know it works</h2><ul class="plain">'
                     + "".join(f"<li>{e(m)}</li>" for m in spec["success_measures"]) + "</ul>"
                     + (f"<p>{e(spec.get('user_experience_notes', '').strip())}</p>" if spec.get("user_experience_notes") else "")
                     + "</section>")

    # flow
    recipes = sorted((d / "recipes").glob("*.json"))
    if recipes:
        parts.append('<section aria-labelledby="flow"><h2 id="flow">How it works</h2>'
                     '<p>Drawn the way the Workato recipe editor shows it. Coloured chips are data passed from earlier steps; ƒ marks a formula.</p>')
        for r in recipes:
            parts.append(rv.render_html(rv.load(r)))
        parts.append("</section>")
    else:
        trig = spec.get("trigger") or {}
        rows = [("Starts when", f"{trig.get('event', '')} ({trig.get('type', '')})"),
                ("Apps used", ", ".join(s.get("app", "") for s in spec.get("systems") or [])),
                ("Volume", f"{(spec.get('volumes') or {}).get('per_day', '?')} per day"),
                ("Speed", (spec.get("sla") or {}).get("latency", "")),
                ("If something goes wrong", (spec.get("error_policy") or {}).get("on_failure", "").strip())]
        parts.append('<section aria-labelledby="flow"><h2 id="flow">How it will work</h2><dl class="kv">'
                     + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in rows if v) + "</dl>"
                     + "<p>The step-by-step recipe flow is drawn at the design approval.</p></section>")
        rules = (spec.get("data") or {}).get("mappings") or []
        if rules:
            parts.append('<section aria-labelledby="rules"><h2 id="rules">Rules it follows</h2><dl class="kv">'
                         + "".join(f"<dt>{e(m.get('to'))}</dt><dd>{e(' '.join(str(m.get('transform', '')).split()))}</dd>" for m in rules)
                         + "</dl></section>")

    # tests
    tests = spec.get("acceptance_tests") or []
    if tests:
        cards = "".join(f"""<div class="test"><span class="id">{e(t.get('id'))}</span>
<dl style="display:contents"><dt>Given</dt><dd>{e(' '.join(str(t.get('given', '')).split()))}</dd>
<dt>Expect</dt><dd>{e(' '.join(str(t.get('expect', '')).split()))}</dd></dl></div>""" for t in tests)
        parts.append(f'<section aria-labelledby="tc"><h2 id="tc">Test cases</h2><p>QA runs each of these with made-up data before anything goes live.</p><div class="tests">{cards}</div></section>')

    # decisions
    qs = spec.get("open_questions") or []
    if qs:
        items = []
        for q in qs:
            if isinstance(q, dict):
                items.append(f"""<div class="q"><b>{e(q.get('id'))} · {e(q.get('question'))}</b>
<span class="rec">{e(q.get('recommendation', ''))}</span>{f'<span class="ans">{e(q.get("answer"))}</span>' if q.get('answer') else ''}</div>""")
            else:
                items.append(f'<div class="q"><b>{e(q)}</b></div>')
        parts.append(f'<section aria-labelledby="dq"><h2 id="dq">Decisions needed from you</h2><div class="qs">{"".join(items)}</div></section>')

    if spec.get("out_of_scope"):
        parts.append('<section aria-labelledby="oos"><h2 id="oos">Not included</h2><ul class="plain">'
                     + "".join(f"<li>{e(x)}</li>" for x in spec["out_of_scope"]) + "</ul></section>")

    last = st["history"][-1]
    parts.append(f"<footer>Stage: {e(stage)} · last change {e(last['at'])} by {e(last['by'])} · source: automations/{e(name)}/</footer>")
    parts.append("</div>" + COPY_JS)
    return "\n".join(parts)


def recipe_page(path: Path, title: str | None = None) -> str:
    doc = rv.load(path)
    t = title or doc.get("name") or path.stem
    return "\n".join([head(t), '<div class="wrap">',
                      f'<header class="top"><span class="eyebrow">Recipe view</span><h1>{e(t)}</h1>'
                      '<p class="lede">How a recipe is shown for review: each step as in the Workato recipe editor, '
                      'with the app, the action, and the fields it uses. Coloured chips are data from earlier steps; ƒ marks a formula.</p></header>',
                      rv.render_html(doc), "</div>"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("automation"); p.add_argument("name")
    p = sub.add_parser("recipe"); p.add_argument("file"); p.add_argument("--out", required=True); p.add_argument("--title")
    a = ap.parse_args()
    if a.cmd == "automation":
        out = ROOT / "automations" / a.name / "review" / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(automation_page(a.name))
    else:
        out = Path(a.out)
        out.write_text(recipe_page(Path(a.file), a.title))
    print(f"wrote {out}")

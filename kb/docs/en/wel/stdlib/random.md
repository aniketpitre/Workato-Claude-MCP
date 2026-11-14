---
url: 'https://docs.workato.com/en/wel/stdlib/random.md'
description: >-
  Use WEL random functions to generate UUIDs, random integers, floats,
  hexadecimal strings, and raw bytes for identifiers and idempotency keys.
---

# Random functions

Random functions generate a new value on every evaluation. Use them for identifiers, such as UUIDs for records without destination-assigned keys, and for idempotency keys that prevent duplicate processing.

> **A RANDOM VALUE ISN'T REPRODUCIBLE**
> 
> Every call returns a different value. A later step can't reproduce a value from an earlier step, and a rerun generates a new value. Store the value in a field and reuse it when downstream steps need it.
> 
> Don't use a random value in anything that must match across systems unless you also store it, for the same reason.

The following examples show the length of each function's output instead of a literal value because each evaluation returns a different value.

Random functions derive their randomness from the host and raise `E450` if the host source fails.

## Identifiers

The following functions generate a fresh identifier suitable for a record or an idempotency key:

### `uuid`

Generates a version 4 UUID as a 36-character string, in the standard `8-4-4-4-12` hyphenated form.

Use `uuid` by default. Its length makes a collision impractical, and every system that accepts an identifier recognizes the format. It takes no arguments.

```wel
uuid()
```

Generate a UUID and measure its length

The following example generates a UUID and measures its length:

**Formula**

```wel
length(uuid())
```

**Output**

```wel
36
```

A generated value looks like `f81d4fae-7dec-41d0-a765-00a0c91e6bf6`.

### `random_hex`

Generates a given number of random bytes and returns them as twice as many hexadecimal characters.

Use it where a system wants an opaque token but doesn't accept the hyphens in a UUID.

```wel
random_hex(bytes)
```

| Parameter | Description |
| --- | --- |
| bytes | How many random bytes to generate. The string returned is twice this long. Non-integer data types raise `E100`. A value outside the `1` to `1,048,576` range raises `E211`. |

Generate a random hex string and measure its length

The following example generates a random hex string and measures its length:

**Formula**

```wel
length(random_hex(16))
```

**Output**

```wel
32
```

## Numbers

The following functions generate a random number within a range:

### `random_int`

Returns a random integer between `min` and `max`, both included.

`min` and `max` must be `Integer` values within the 64-bit signed integer range. Non-integer data types raise `E100`. A value outside the 64-bit signed integer range raises `E211`. Values that set `max` less than `min` raise `E211` instead of swapping the bounds. `random_int` returns the shared value when `min` and `max` are equal.

```wel
random_int(min, max)
```

| Parameter | Description |
| --- | --- |
| min | Lowest possible value, included. |
| max | Highest possible value, included. |

### `random_float`

Returns a random `Float` between `0.0` and `1.0`, including the lower bound but excluding the upper. The result is uniform over multiples of 2^-53.

Don't use `random_float` for anything requiring exact decimal arithmetic, because it returns a `Float`. Refer to [Data types](/en/wel/language/data-types). It takes no arguments.

```wel
random_float()
```

## Raw bytes

The following function generates raw random bytes, for a salt or an initialization vector:

### `random_bytes`

Returns a given number of random bytes as a `Binary` value.

Use it where you genuinely need a byte sequence, such as a salt or an initialization vector for [crypto functions](/en/wel/stdlib/crypto). `random_hex` or `uuid` gives you a string directly for an identifier you intend to put in a field or a URL.

```wel
random_bytes(count)
```

| Parameter | Description |
| --- | --- |
| count | How many bytes to generate. Non-integer data types raise `E100`. A value outside the `1` to `1,048,576` range raises `E211`. |

Generate random bytes and measure their length

The following example generates random bytes and measures their length:

**Formula**

```wel
byte_length(random_bytes(8))
```

**Output**

```wel
8
```

## Related

- [Crypto functions](/en/wel/stdlib/crypto): Information about using random bytes as salts and initialization vectors.
- [Binary functions](/en/wel/stdlib/binary): Information about `byte_length`, and how to turn `Binary` into hex or base64 text.
- [Data types](/en/wel/language/data-types): Information about `Binary`, `Float`, and `Decimal`.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E100`, `E211`, and `E450`.

---

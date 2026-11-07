---
url: 'https://docs.workato.com/en/formulas/string-formulas.md'
description: >-
  Reference for Workato string formulas, allowlisted Ruby methods that
  manipulate text with conditionals, formatting, and substring checks.
---

# String formulas

In Ruby, strings refer to sequences of text and characters. Workato supports a variety of string formulas.

Formulas in Workato are allowlisted Ruby methods. Syntax and functionality for these formulas are generally unchanged. Most formulas return an error and stop the job if the formula operates on nulls (expressed as `nil` in Ruby), except for `present?`, `presence`, and `blank?`.

You can refer to the Ruby documentation on [strings](https://ruby-doc.org/core-2.3.3/String.html) for more information. However, only allowlisted Ruby methods are supported. Contact your Customer Success Manager to request new formulas for the allowlist.

The following examples show methods that can be used to manipulate a string in Workato.

* * *

## Conditionals

This section covers conditional formulas for strings. Refer to [Conditions](/en/formulas/conditions) for the full conditions reference.

* * *

### `blank?`

Checks whether the input is considered blank according to Ruby conventions. This includes:

- Null values
- Empty inputs
- False booleans
- Strings containing only whitespace
- Non-value numbers, sometimes referred to as NaN (not a number). This is an undefined value or value that cannot be represented. For example, the result of division by zero, or a missing value.

#### Syntax

Input.blank?

- Input - An input datapill. It can be a string, number, date, datetime, boolean, array, or object datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".blank? | false |
| 123.blank? | false |
| 0.blank? | false |
| "".blank? | true |
| ' '.blank? | true |
| nil.blank? | true |
| false.blank? | true |
| true.blank? | false |
| \[\].blank? | true |
| {}.blank? | true |

#### How it works

If the input is considered blank according to Ruby conventions, the formula returns true. For any other data, it returns false.

#### See also

- [presence](/en/formulas/string-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [present?](/en/formulas/string-formulas#present): Returns true if there is a valid input.

* * *

### `is_not_true?`

Evaluates a boolean value and returns true if the evaluated value is not true.

#### Syntax

Input.is\_not\_true?

- Input - An input boolean, an integer (`1` or `0`), or an accepted string value.

#### Sample usage

| Formula | Result |
| --- | --- |
| true.is\_not\_true? | false |
| false.is\_not\_true? | true |
| 0.is\_not\_true? | true |
| nil.is\_not\_true? | true |

#### How it works

Takes in an input and evaluates if it is true or false.

> **String values**
> 
> `"true"`, `"t"`, `"yes"`,`"y"`, and `"1"` are evaluated as a boolean **true**.
> 
> `"false"`, `"f"`, `"no"`,`"n"`, and `"0"` are evaluated as a boolean **false**.
> 
> However, an empty string (`""`) is not evaluated as a boolean. This formula will display an error if used on a string datatype.

#### See also

- [is\_true](/en/formulas/string-formulas#is-true): Evaluates a boolean value and returns true if the evaluated value is true.

* * *

### `is_true?`

Evaluates a boolean value and returns true if the evaluated value is true.

#### Syntax

Input.is\_true?

- Input - An input boolean, an integer (`1` or `0`), or an accepted string value.

#### Sample usage

| Formula | Result |
| --- | --- |
| true.is\_true? | true |
| false.is\_true? | false |
| 0.is\_true? | false |
| nil.is\_true? | false |

#### How it works

Takes in an input and evaluates if it is true or false.

> **String values**
> 
> `"true"`, `"t"`, `"yes"`,`"y"`, and `"1"` are evaluated as a boolean **true**.
> 
> `"false"`, `"f"`, `"no"`,`"n"`, and `"0"` are evaluated as a boolean **false**.
> 
> However, an empty string (`""`) is not evaluated as a boolean. This formula will display an error if used on a string datatype.

#### See also

- [is\_not\_true](/en/formulas/string-formulas#is-not-true): Evaluates a boolean value and returns true if the evaluated value is not true.

* * *

### `present?`

This formula will check the input and if there is a value present, it will return true. If the input is nil, boolean false, an empty string, or an empty list, the formula will return false.

#### Syntax

Input.present?

- Input - An input datapill. It can be a string, number, date, or list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".present? | true |
| 123.present? | true |
| 0.present? | true |
| "2017-04-02T12:30:00.000000-07:00".present? | true |
| nil.present? | false |
| "".present? | false |
| \[\].present? | false |

#### How it works

If the input is null, an empty string or an empty list, the formula will return false. For any other data, it returns true.

> **Evaluating a list with nil values**
> 
> - Only an empty list will return false.
> 
> \[\].present? returns false.
> 
> - A list with nil and empty string will return true.
> 
> \[nil,""\].present? returns true.

#### See also

- [presence](/en/formulas/string-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [blank?](/en/formulas/string-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.

* * *

### `presence`

Returns the data if it exists, returns nil if it does not.

#### Syntax

Input.presence

- Input - An input datapill. It can be a string, number, date, or datetime datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| nil.presence | nil |
| "".presence | nil |
| "Any Value".presence | "Any Value" |
| 45.0.presence | 45.0 |
| 0.presence | 0 |

#### How it works

If the input is null or an empty string, the formula will return nil. For any other data, it returns the original input data.

#### See also

- [blank?](/en/formulas/string-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.
- [present?](/en/formulas/string-formulas#present): Returns true if there is a valid input.

* * *

### `include?`

Checks if the string contains a specific substring. Returns true if it does.

#### Syntax

Input.include?(substring)

- Input - A string input.
- substring - The substring to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Partner account".include?("Partner") | true |
| "Partner account".include?("partner") | false |

#### How it works

This formula checks if the string contains a specific substring. The formula returns true if the string includes the substring and false if does not. The substring is case sensitive.

This formula acts in the opposite manner from [exclude?](/en/formulas/string-formulas#exclude). The formula returns true only if the input string contains the stated keyword.

#### See also

- [exclude?](/en/formulas/string-formulas#exclude): Checks if the string contains a specific substring. Returns false if it does.

* * *

### `exclude?`

Checks if the string contains a specific substring. Returns false if it does.

#### Syntax

Input.exclude?(substring)

- Input - A string input.
- substring - The substring to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Partner account".exclude?("Partner") | false |
| "Partner account".exclude?("partner") | true |

#### How it works

This formula check is the string contains a specific substring. Returns false if it does, otherwise, returns true. This substring is case sensitive.

This function acts in an opposite manner from [include?](/en/formulas/string-formulas#include). It will return true only if the input string does NOT contain the stated keyword.

#### See also

- [include?](/en/formulas/string-formulas#include): Checks if the string contains a specific substring. Returns true if it does.

* * *

### `match?`

Checks if the string contains a specific regular expression (regex) pattern. Returns true if it does.

#### Syntax

Input.match?(pattern)

- Input - A string input.
- pattern - The regex pattern to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".match?(/Marie/) | true |
| "Jean Marie".match?(/ /) | true |
| "Partner account".match?(/partner/) | false |

#### How it works

This formula checks if the string contains a specific regex pattern. Returns true if it does, otherwise, returns false.

#### See also

- [include?](/en/formulas/string-formulas#include): Checks if the string contains a specific substring. Returns true if it does.
- [exclude?](/en/formulas/string-formulas#exclude): Checks if the string contains a specific substring. Returns false if it does.

* * *

### `ends_with?`

Checks if the string ends with a specific substring. Returns true if it does.

#### Syntax

Input.ends\_with?(substring)

- Input - A string input.
- substring - The substring to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".ends\_with?("rie") | true |
| "Jean Marie".ends\_with?("RIE") | false |
| "Jean Marie".upcase.ends\_with?("RIE") | true |

#### How it works

This formula check is the string ends with a specific substring. Returns true if it does, otherwise, returns false.

#### See also

- [include?](/en/formulas/string-formulas#include): Checks if the string contains a specific substring. Returns true if it does.
- [exclude?](/en/formulas/string-formulas#exclude): Checks if the string contains a specific substring. Returns false if it does.
- [match?](/en/formulas/string-formulas#match): Checks if the string contains a specific pattern. Returns true if it does.
- [starts\_with?](/en/formulas/string-formulas#starts-with): Checks if the string starts with a specific substring. Returns true if it does.

* * *

### `starts_with?`

Checks if the string starts with a specific substring. Returns true if it does.

#### Syntax

Input.starts\_with?(substring)

- Input - A string input.
- substring - The substring to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".starts\_with?("Jean") | true |
| "Jean Marie".starts\_with?("JEAN") | false |
| "Jean Marie".upcase.starts\_with?("JEAN") | true |

#### How it works

This formula check is the string starts with a specific substring. Returns true if it does, otherwise, returns false.

#### See also

- [include?](/en/formulas/string-formulas#include): Checks if the string contains a specific substring. Returns true if it does.
- [exclude?](/en/formulas/string-formulas#exclude): Checks if the string contains a specific substring. Returns false if it does.
- [match?](/en/formulas/string-formulas#match): Checks if the string contains a specific pattern. Returns true if it does.
- [ends\_with?](/en/formulas/string-formulas#ends-with): Checks if the string ends with a specific substring. Returns true if it does.

* * *

## Text manipulation

This section contains formulas which allow you to manipulate text within strings.

* * *

### `parameterize`

Replaces special characters in a string with standard characters. Used when app does not accept non-standard characters.

#### Syntax

Input.parameterize

- Input - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "öüâ".parameterize | "oua" |

#### How it works

This formula searches for all special characters in the string and replaces them with standard characters.

* * *

### `lstrip`

This formula removes the white space at the beginning of the input string.

#### Syntax

String.lstrip

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| " Test ".lstrip | "Test " |

#### How it works

This formula removes white spaces from the beginning of a string. If the string doesn't have any white spaces before, the input string will be returned as is.

> **SELECTIVELY REMOVE WHITE SPACES**
> 
> - To remove white spaces from the end of a string, use [rstrip](/en/formulas/string-formulas#rstrip).
> - To remove white spaces from the middle of a string, use [gsub](/en/formulas/string-formulas#gsub).  
>   "a b c d e".gsub(" " , "") returns `"abcde"`.

#### See also

- [strip](/en/formulas/string-formulas#strip): Removes the white space at the beginning and the end of the input string.
- [rstrip](/en/formulas/string-formulas#rstrip): Removes the white space at the end of the input string.
- [gsub](/en/formulas/string-formulas#gsub): Replace parts of a text string. Returns a new string with the replaced characters.

* * *

### `rstrip`

This formula removes the white space at the end of the input string.

#### Syntax

String.rstrip

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| " Test ".rstrip | " Test" |

#### How it works

This formula removes white spaces from the end of a string. If the string doesn't have any white spaces at the end, the input string will be returned as is.

> **SELECTIVELY REMOVE WHITE SPACES**
> 
> - To remove only white spaces from the beginning of a string, use [lstrip](/en/formulas/string-formulas#lstrip).
> - To remove white spaces from the middle of the string, use [gsub](/en/formulas/string-formulas#gsub).  
>   "a b c d e".gsub(" " , "") returns `"abcde"`.

#### See also

- [strip](/en/formulas/string-formulas#rstrip): Removes the white space at the beginning and the end of the input string.
- [lstrip](/en/formulas/string-formulas#lstrip): Removes the white space at the beginning of the input string.
- [gsub](/en/formulas/string-formulas#gsub): Replace parts of a text string. Returns a new string with the replaced characters.

* * *

### `scrub`

If the string is an invalid byte sequence, the formula replaces the invalid bytes with a replacement character. If the string is not invalid, the formula returns the original string.

#### Syntax

String.scrub(replacement string)

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "abc\\u3042\\x81".scrub("\*") | "abc\\u3042\*" |

* * *

### `strip`

This formula removes the white space at the beginning and end of the input string.

#### Syntax

String.strip

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Welcome to the future of automation! ".strip | "Welcome to the future of automation!" |
| " This is an example ".strip | "This is an example" |

#### How it works

This formula removes white spaces from both sides of a string. If the string doesn't have any white spaces on either side, the input string will be returned as is.

> **SELECTIVELY REMOVE WHITE SPACES**
> 
> - To remove only white spaces from one side, use [lstrip](/en/formulas/string-formulas#lstrip) or [rstrip](/en/formulas/string-formulas#rstrip).
> - To remove white spaces from the middle of the string, use [gsub](/en/formulas/string-formulas#gsub).  
>   "a b c d e".gsub(" " , "") returns `"abcde"`.

#### See also

- [lstrip](/en/formulas/string-formulas#lstrip): Removes the white space at the beginning of the input string.
- [rstrip](/en/formulas/string-formulas#rstrip): Removes the white space at the end of the input string.
- [gsub](/en/formulas/string-formulas#gsub): Replace parts of a text string. Returns a new string with the replaced characters.

* * *

### `strip_tags`

This formula removes HTML tags embedded in a string.

#### Syntax

String.strip\_tags

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "<p>Jean Marie</p>"..strip\_tags | "Jean Marie" |

#### How it works

This formula checks for HTML tags within the input string. It removes any HTML tags found and returns the string.

#### See also

- [strip](/en/formulas/string-formulas#rstrip): Removes the white space at the beginning and the end of the input string.

* * *

### `ljust`

Aligns the string to left and pads it with whitespace or the provided character/string until the string is a specified length.

#### Syntax

String.ljust(length,character)

- String - An input string.
- length - The length of the output string.
- character - (optional) The character or string used to pad the input string. If unspecified, the default pad character is a blank space.

#### Sample usage

| Formula | Result |
| --- | --- |
| "test".ljust(5) | "test " |
| "test".ljust(10, "\*") | "test\*\*\*\*\*\*" |
| "test".ljust(9, "12345") | "test12345" |

#### See also

- [rjust](/en/formulas/string-formulas#rjust): Aligns the string to right and pads with whitespace or the provided string until string is specified length.

* * *

### `rjust`

Aligns the string to left and pads it with whitespace or a provided character/string until string is a specified length.

#### Syntax

String.rjust(length,character)

- String - An input string.
- length - The length of the output string.
- character - (optional) The character or string padding the input string. If unspecified, the default pad character is a blank space.

#### Sample usage

| Formula | Result |
| --- | --- |
| "test".rjust(5) | " test" |
| "test".rjust(10, "\*") | "\*\*\*\*\*\*test" |
| "test".rjust(9, "12345") | "12345test" |

#### See also

- [ljust](/en/formulas/string-formulas#ljust): Aligns the string to left and pads it with whitespace or the provided string until string is a specified length.

* * *

### `reverse`

Inverts a string, reordering the characters in reverse order. Case is preserved.

#### Syntax

String.reverse

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".reverse | "eiraM naeJ" |
| " jean marie ".reverse | " eiram naej " |

* * *

### `gsub`

Replace parts of a text string. Returns a new string with the replaced characters.

#### Syntax

String.gsub(find,replace)

- String - An input string. You can use a datapill or a static string value.
- find - The string or regular expression (regex) to look for. Use a `/pattern/` syntax for regex.
- replace - The replacement string. You can define the replacement using a string or [hash](/en/formulas/array-list-formulas#hashes).

#### Sample usage

| Formula | Result |
| --- | --- |
| "I have a blue house and a blue car".gsub("blue", "red") | "I have a red house and a red car" |
| "Jean Marie".gsub("J", "M") | "Mean Marie" |
| "Jean Marie".gsub(/\[Jr\]/, 'M') | "Mean MaMie" |
| "Jean Marie".downcase.gsub("j", "M") | "Mean marie" |

#### Advanced sample usage

Learn more about advanced usage for the `gsub` method from the [Ruby documentation](https://ruby-doc.org/core-2.7.2/String.html#method-i-gsub.)

| Formula | Result |
| --- | --- |
| "Awesome".gsub(/\[Ae\]/, 'A'=>'E', 'e'=>'a') | "Ewasoma" |
| "Anna's Cafe".gsub("'", "\\\\'") | "Annas Cafes Cafe" This replaces the quotation symbol with text after the breakpoint. |
| "Anna's Cafe".gsub("'", {"'"=>"\\\\'"}) | "Anna\\\\'s Cafe" This replace the quotation symbol with a replacement string. |

#### How it works

This formula is similar to find and replace. It takes two input parameters:

- **First input**: The string that you plan to replace. The input is case-sensitive, so make sure to input uppercase or lowercase correctly to find all occurrences that are an exact match.
- **Second input**: The new string that replaces all occurrences of the first input.

#### See also

- [sub](/en/formulas/string-formulas#sub): Replaces the first occurrence of a search term.

* * *

### `sub`

Replaces the first occurrence of the first input value, with the second input value, within the string. This formula is case-sensitive - make sure to type in uppercase or lowercase before comparison if you are concerned about case sensitivity.

#### Syntax

String.sub(find,replace)

- String - An input string. You can use a datapill or a static string value.
- find - The string or regular expression (regex) to look for. Use a `/pattern/` syntax for regex.
- replace - The replacement string. You can define the replacement using a string or [hash](/en/formulas/array-list-formulas#hashes).

#### Sample usage

| Formula | Result |
| --- | --- |
| "Mean Marie".sub(/M/, "J") | "Jean Marie" |
| "Hello".sub(/\[aeiou\]/, "\*") | "H\*llo" |

* * *

### `length`

Returns the number of characters within an input string, including whitespaces.

#### Syntax

String.length

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".length | 10 |
| " jean marie ".length | 12 |

* * *

### `slice`

Returns a partial segment of a string.

#### Syntax

String.slice(start,end)

- String - An input string.
- start - The index of the string to start returning a partial segment at. Strings are zero-indexed.
- end - (optional) The number of characters to return. If unspecified, the formula will return only one character.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Jean Marie".slice(0,3) | "Jea" |
| "Jean Marie".slice(5) | "M" |
| "Jean Marie".slice(3,3) | "n M" |
| "Jean Marie".slice(-5,5) | "Marie" |

#### How it works

The formula returns a partial segment of a string. It takes in two parameters - the first parameter is the index that decides which part of the string to start returning from. The first letter of a string corresponds to an index of 0. Negative numbers start from the last character, so an index of -1 is the last character in the string. The second parameter decides how many characters to return. If you only pass in the first parameter, one character is returned.

* * *

### `scan`

Scan the string for the regex pattern to retrieve and returns an array.

#### Syntax

String.scan(pattern)

- String - An input string.
- regex pattern - The regex pattern to search for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Thu, 01/23/2014".scan(/\\d+/) | \["01","23","2014"\] |
| "Thu, 01/23/2014".scan(/\\d+/).join("-") | "01-23-2014" |

* * *

### `encode`

Returns the string encoded.

#### Syntax

String.encode(encoding)

- String - An input string.
- encoding - Name of the encoding (for example, Windows-1252). Refer to the [Ruby Programming/Encoding](https://en.wikibooks.org/wiki/Ruby_Programming/Encoding) Wikibooks article for more information on ruby encodings.

#### Sample usage

| Formula | Result |
| --- | --- |
| `"Jean Marie"`.encode("Windows-1252") | "Jean Marie" |
| `"Olé!"`.encode("UTF-8") | `"Olé!"` |
| `"Olé"`.encode("ASCII") | "Error calculating input: U+00E9 from UTF-8 to US-ASCII" |

* * *

### `transliterate`

Replaces non-ASCII characters with an ASCII approximation. If no approximation exists, it uses a replacement character which defaults to '?'.

#### Syntax

String.transliterate

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Chloé".transliterate | "Chloe" |

- [parameterize](/en/formulas/string-formulas#parameterize): Replaces special characters in a string.

* * *

## Text case manipulation

This section covers formulas which allow you to change the case of certain parts of a word.

* * *

### `capitalize`

Converts the input string into sentence case, where the first character of the string is capitalized and all other characters are lowercase.

#### Syntax

String.capitalize

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "ticket opened. Gold SLA".capitalize | "Ticket opened. gold sla" |
| "jean MARIE".capitalize | "Jean marie" |

* * *

### `titleize`

Converts the input string into title case, where the first character of each word is capitalized and all other characters are lowercase.

#### Syntax

String.titleize

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "ticket opened. Gold SLA".titleize | "Ticket Opened. Gold Sla" |
| "jean MARIE".titleize | "Jean Marie" |

* * *

### `upcase`

Convert text to uppercase.

#### Syntax

String.upcase

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Automation at its FINEST!".upcase | "AUTOMATION AT ITS FINEST!" |
| "Convert to UPCASE".upcase | "CONVERT TO UPCASE" |

#### How it works

This formula searches for any lowercase character and replace it with the uppercase characters.

> **USE UPCASE TO IMPROVE STRING SEARCHES**
> 
> Search formulas like ([gsub](/en/formulas/string-formulas#gsub) or [sub](/en/formulas/string-formulas#sub)) use case sensitive characters. Use the `upcase` formula to ensure that all characters are in the same case before searching.

#### See also

- [downcase](/en/formulas/string-formulas#downcase): Convert text to lowercase.
- [capitalize](/en/formulas/string-formulas#capitalize): Convert text to sentence case.
- [titleize](/en/formulas/string-formulas#titleize): Convert text to title case.

* * *

### `downcase`

Convert text to lowercase.

Video tutorial: Downcase formula use case

[Video](https://www.youtube.com/embed/HXBe9PVwH0M)

#### Syntax

String.downcase

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Automation at its FINEST!".downcase | "automation at its finest!" |
| "Convert to DOWNCASE".downcase | "convert to downcase" |

#### How it works

This formula searches for any uppercase character and replace it with the lowercase characters.

> **USE DOWNCASE TO IMPROVE STRING SEARCHES**
> 
> Search formulas like ([gsub](/en/formulas/string-formulas#gsub) or [sub](/en/formulas/string-formulas#sub)) use case sensitive characters. Use the `downcase` formula to ensure that all characters are in the same case before searching.

#### See also

- [upcase](/en/formulas/string-formulas#upcase): Convert text to uppercase.
- [capitalize](/en/formulas/string-formulas#capitalize): Convert text to sentencecase.
- [titleize](/en/formulas/string-formulas#titleize): Convert text to titlecase.

* * *

### `quote`

Quotes a string, escaping any ' (single quote) characters

#### Syntax

String.quote

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Paula's Baked Goods".quote | "Paula's Baked Goods" |

* * *

## Converting to arrays and back

This section shows how you can manipulate strings into arrays.

* * *

### `split`

This formula divides a string around a specified character and returns an array of strings.

Watch a step-by-step video tutorial instead

[Video](https://www.youtube.com/embed/trpODHgNzCY)

#### Syntax

String.split(char)

- String - An input string value. You can use a datapill or a static value.
- char - (optional) The character to split the text at. This is case sensitive. If no character is defined, then by default, strings are split by white spaces.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Ms-Jean-Marie".split("-") | \["Ms", "Jean", "Marie"\] |
| "Ms Jean Marie".split | \["Ms", "Jean", "Marie"\] |
| "Split string".split() | \["Split", "string"\] |
| "Split string".split("t") | \["Split", " s", "ring"\] |
| "01/23/2014".split("/") | \["01", "23", "2014"\] |
| "01/23/2014".split("/").join("-") | "01-23-2014" |

#### How it works

This formula looks for the specified character in the input string. Every time it is found, the input will be split into a new string.

> **Split characters**
> 
> You can use a string of characters together as the split argument (for example, `"and"`).
> 
> "You and Me".split(`"and"`) returns `["You","Me"]`.

#### See also

- [strip](/en/formulas/string-formulas#strip): Removes white space around the input string.
- [slice](/en/formulas/string-formulas#slice): Returns a partial segment of a string.
- [match](/en/formulas/string-formulas#match): Checks the input string for a particular pattern.
- [join](/en/formulas/array-list-formulas#join): Combines list items into a string.

* * *

### `bytes`

Returns an array of bytes for a given string.

#### Syntax

String.bytes

- String - An input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Hello".bytes | \["72", "101", "108", "108", "111"\] |

* * *

### `bytesize`

Returns the length of a given string in bytes.

#### Syntax

Input.bytesize

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Hello".bytesize | 5 |

* * *

### `byteslice`

Returns a substring of specified bytes instead of length. In some cases, non ASCII characters such as Japanese or Chinese may use multiple bytes.

#### Syntax

Input.byteslice(0,4)

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "hello".byteslice(1) | e |
| "hello".byteslice(-1) | o |
| "hello".byteslice(1,2) | el |
| "abc漢字".byteslice(0,4) | abc漢 |

* * *

## Conversion of other data types to strings

* * *

### `to_s`

Converts non-string data types such as numbers or dates to a string (text) datatype.

Video tutorial: to\_s formula use case

[Video](https://www.youtube.com/embed/nOkGS8fYv5g)

#### Syntax

Input.to\_s

- Input - Any input data. You can use number, array, object, or datetime datatypes.

#### Sample usage

| Formula | Result |
| --- | --- |
| \-45.67.to\_s | "-45.67" |
| "123".to\_s | "123" |
| \[1, 2, 3\].to\_s | "\[1, 2, 3\]" |
| {key: "Workato"}.to\_s | "{:key=>"Workato"}" |
| "2020-06-05T17:13:27.000000-07:00".to\_s | "2020-06-05T17:13:27.000000-07:00" |
| "2020-06-05T17:13:27.000000-07:00".to\_s(:short) | "05 Jun 17:13" |
| "2020-06-05T17:13:27.000000-07:00".to\_s(:long) | "June 05, 2020 17:13" |

#### How it works

This formula returns a string representation of the input data.

> **OUTPUT IS A STRING DATATYPE**
> 
> A string representation of a list cannot be used in a [**repeat step**](/en/recipes/steps#repeat-step).

#### See also

- [to\_f](/en/formulas/string-formulas#to-f): Converts data to a float (number) datatype.
- [to\_i](/en/formulas/string-formulas#to-i): Converts data to an integer (whole number) datatype.

* * *

### `ordinalize`

Turns a number into an ordinal string used to denote the position in an ordered sequence, such as 1st, 2nd, 3rd, 4th.

#### Syntax

Input.ordinalize

- Input - Any input number.

#### Sample usage

| Formula | Result |
| --- | --- |
| 1.ordinalize | "1st" |
| 2.ordinalize | "2nd" |
| 3.ordinalize | "3rd" |
| 1003.ordinalize | "1003rd" |
| \-3.ordinalize | "-3rd" |

* * *

## Conversion of strings to other data types

* * *

### `to_f`

Converts data to a float (number) datatype.

#### Syntax

Input.to\_f

- Input - Numerical input data. You can use a string datatype or a integer datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| 45.to\_f | 45.0 |
| \-45.to\_f | \-45.0 |
| "45.67".to\_f | 45.67 |
| "Workato".to\_f | 0 |

#### How it works

This formula checks if the input contains any numbers. If no numbers are found, it returns 0. If the number does not have a decimal point, `.0` is added to the number.

#### See also

- [to\_i](/en/formulas/string-formulas#to-i): Convert data to an integer (whole number) datatype.

* * *

### `to_i`

Converts data to an integer (whole number) datatype.

#### Syntax

Input.to\_i

- Input - Numerical input data. You can use a string datatype or a float datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| 45.43.to\_i | 45 |
| \-45.43.to\_i | \-45 |
| "123".to\_i | 123 |
| "Workato".to\_i | 0 |

#### How it works

This formula checks if the input contains any numbers. If no numbers are found, it returns 0. If the number has a decimal point, everything after the decimal is omitted.

> **CHECK FOR INTEGERS**
> 
> You can use this formula to check if a string contains an integer. If the input does not contain any numbers, the formula returns `0`.

#### See also

- [to\_f](/en/formulas/string-formulas#to-f): Converts data to a float (number) datatype.

* * *

### `to_country_alpha2`

Convert an alpha-3 country code or country name to an alpha-2 country code (first 2 initials).

#### Syntax

Input.to\_country\_alpha2

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GBR".to\_country\_alpha2 | "GB" |
| "United Kingdom".to\_country\_alpha2 | "GB" |

* * *

### `to_country_alpha3`

Convert alpha-2 country code or country name to an alpha-3 country code (first 3 initials).

#### Syntax

Input.to\_country\_alpha3

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GB".to\_country\_alpha3 | "GBR" |
| "United Kingdom".to\_country\_alpha3 | "GBR" |

* * *

### to\_country\_name

Convert alpha-2, alpha-3 country code, or country name to ISO3166 country name.

#### Syntax

Input.to\_country\_name

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GBR".to\_country\_name | "United Kingdom" |
| "GB".to\_country\_name | "United Kingdom" |

* * *

### `to_currency`

Formats integers or numbers to a currency-style, adding a default currency symbol at the start of the string.

#### Syntax

Input.to\_currency

- Input - Any input string.

#### Sample usage

| Formula | Description | Result |
| --- | --- | --- |
| "345.60".to\_currency | Adds default currency symbol "$" | "$345.60" |

#### Advanced sample usage

Learn more about advanced use of the to\_currency formula. A comma-separated combination of these may be used to achieve the desired currency format. For example:

```ruby
"12345.678".to_currency(delimiter: ".", format: "%n %u", precision: 2, separator: ",", unit: "€")
```

| Formula | Description | Result |
| --- | --- | --- |
| "345.60".to\_currency(unit: "€") | Changes the default currency unit | "€345.60" |
| "345.60".to\_currency(format: "%n %u") | Changes the position of the number relative to the unit (where the number is represented by `%n` and the currency unit is represented by `%u`). Accepts 0 or 1 spaces in between. Defaults to `"%u%n"`. | "345.60 $" |
| "-345.60".to\_currency(negative\_format: "(%u%n)") | Specifies the format when the number is negative (where the number is represented by `%n` and the currency unit is represented by `%u`). | "($345.60)" |
| "345.678".to\_currency | Precision defaults to 2 decimal places | "$345.68" |
| "345.678".to\_currency(precision: 3) | Change the precision by specifying the number of decimal places | "$345.678" |
| "345.678".to\_currency(separator: ",") | Specify the **decimal separator** as ".", "," or " ". Defaults to ".". | "$345,68" |
| "12345.678".to\_currency(delimiter: ".") | Specify the **thousands separator** as ",", "." or " ". Defaults to ",". | "$12.345.68" |

* * *

### `to_currency_code`

Convert alpha-2, alpha-3 country code, or country name to ISO4217 currency code

#### Syntax

Input.to\_currency\_code

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GBR".to\_currency\_code | "GBP" |
| "US".to\_currency\_code | "USD" |

* * *

### `to_currency_name`

Convert alpha-3 currency code or alpha-2/3 country code or country name to ISO4217 currency name.

#### Syntax

Input.to\_currency\_name

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GBR".to\_currency\_code | "Pound" |
| "USD".to\_currency\_code | "Dollars" |

* * *

### `to_currency_symbol`

Convert alpha-3 currency code or alpha-2/3 country code or country name to ISO4217 currency symbol.

#### Syntax

Input.to\_currency\_symbol

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "GBR".to\_currency\_symbol | "£" |
| "USD".to\_currency\_symbol | "$" |

* * *

### `to_phone`

Converts string or number to a formatted phone number (user-defined).

#### Syntax

Input.to\_phone

- Input - Any input string or number.

#### Sample usage

| Formula | Result |
| --- | --- |
| "5551234".to\_phone | 555-1234 |
| 1235551234.to\_phone | 123-555-1234 |
| 1235551234.to\_phone(area\_code: true) | (123) 555-1234 |
| 1235551234.to\_phone(delimiter: " ") | 123 555 1234 |
| 1235551234.to\_phone(area\_code: true, extension: 555) | (123) 555-1234 x 555 |
| 1235551234.to\_phone(country\_code: 1) | +1-123-555-1234 |
| "123a456".to\_phone | 123a456 |

* * *

### `to_state_code`

Convert state name to code.

#### Syntax

Input.to\_state\_code

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "California".to\_state\_code | CA |

* * *

### `to_state_name`

Convert state code to name.

#### Syntax

Input.to\_state\_name

- Input - Any input string.

#### Sample usage

| Formula | Result |
| --- | --- |
| "CA".to\_state\_name | CALIFORNIA |

* * *

---

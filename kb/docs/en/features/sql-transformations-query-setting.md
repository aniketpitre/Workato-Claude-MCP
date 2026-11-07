---
url: 'https://docs.workato.com/en/features/sql-transformations-query-setting.md'
description: >-
  Set up your SQL query and parameters for SQL Transformations, powered by the
  Apache DataFusion engine with support for joins and standard SQL.
---

# Set up your query

After you've [set up your data source](/en/features/sql-transformations-data-source-setting), continue with SQL Transformations by setting up your query.

## Set up your query

After specifying a data source, you can define the query that acts on the data. SQL Transformations is powered by the [Apache DataFusion](https://datafusion.apache.org/) query engine and supports all standard SQL operations.

Configure the following fields:

| Field | Description |
| --- | --- |
| Query parameters | Add the parameters to use in the `WHERE` condition of your query. For example, `id`. Assign a value to each parameter, which can be static or a datapill. Select the closest corresponding data type that your database expects for the bind variable. |
| SQL query | Add a SQL select statement to query one or more data sources. Joins and complex functions are supported. Use bind variables notation to add parameters in the `WHERE` condition For example, `id = @id`, where `id` is the field name in the **Query parameters** section. |
| Engine | Select the [Apache DataFusion](https://datafusion.apache.org/) engine version that executes your query. The default is **DataFusion v53**. Select **DataFusion v42** if your existing queries require the previous engine version. Refer to the [Apache DataFusion 53.0.0 release notes](https://datafusion.apache.org/blog/2026/04/02/datafusion-53.0.0/) for details on changes in v53. |

## Example query setup

The following query merges the employee and zipcode tables together based on the zipcode column in both tables.

![Example query setup](/assets/query.DrLw69nV.png)_Example query setup_

> **CAPITALIZATION**
> 
> In the preceding example, all of the CSV headers are lowercase. If your query contains capitalized CSV headers, you must enclose the capitalized headers in quotation marks (`""`). For example:
> 
> ```sql
> SELECT distinct test."PropertyId", test."Tract_Business" FROM test ORDER by test."PropertyId" LIMIT 1 OFFSET 2
> ```

* * *

## Supported operations

The following section contains lists of supported and unsupported data types, syntax clauses, subqueries, and functions in SQL Transformations.

### Data types

Character types

- CHAR
- VARCHAR
- TEXT
- STRING

Numeric types

- TINYINT
- SMALLINT
- INT or INTEGER
- BIGINT
- TINYINT UNSIGNED
- SMALLINT UNSIGNED
- INT UNSIGNED or INTEGER UNSIGNED
- BIGINT UNSIGNED
- FLOAT
- REAL
- DOUBLE
- DECIMAL(precision, scale)

Date/Time types

- DATE
- TIME
- TIMESTAMP
- INTERVAL

Boolean types

- BOOLEAN

Binary types

- BYTEA

Arrow types

- Null
- Boolean
- Int8
- Int16
- Int32
- Int64
- UInt8
- UInt16
- UInt32
- UInt64
- Float16
- Float32
- Float64
- Utf8
- LargeUtf8
- Binary
- Timestamp(Second, None)
- Timestamp(Millisecond, None)
- Timestamp(Microsecond, None)
- Timestamp(Nanosecond, None)
- Time32
- Time64
- Duration(Second)
- Duration(Millisecond)
- Duration(Microsecond)
- Duration(Nanosecond)
- Interval(YearMonth)
- Interval(DayTime)
- Interval(MonthDayNano)
- FixedSizeBinary(<len>)
  - Example: FixedSizeBinary(16)
- Decimal128(<precision>, <scale>)
  - Example: Decimal128(3, 10)
- Decimal256(<precision>, <scale>)
  - Example: Decimal256(3, 10)

* * *

### Unsupported data types

Unsupported types

- UUID
- BLOB
- CLOB
- BINARY
- VARBINARY
- REGCLASS
- NVARCHAR
- CUSTOM
- ARRAY
- ENUM
- SET
- DATETIME

* * *

### SELECT syntax clauses

SELECT syntax clauses supported

- WITH
- SELECT
- FROM
- WHERE
- JOIN
  - INNER JOIN
  - LEFT OUTER JOIN
  - RIGHT OUTER JOIN
  - FULL OUTER JOIN
  - NATURAL JOIN
  - CROSS JOIN
- GROUP BY
- HAVING
- UNION
- ORDER BY
- LIMIT
- EXCLUDE and EXCEPT

* * *

### Subqueries

SELECT subqueries supported

- EXISTS
- NOT EXISTS
- IN
- NOT IN
- Scalar Subquery

* * *

### Operators

Numerical operators

- `+` (plus)
- `-` (minus)
- `*` (multiply)
- `/` (divide)
- `%` (modulo)

Comparison operators

- `=` (equal)
- `!=` (not equal)
- `<` (less than)
- `<=` (less than or equal to)
- `>` (greater than)
- `>=` (greater than or equal to)
- IS DISTINCT FROM
- IS NOT DISTINCT FROM
- `~` (regex match)
- `~*` (regex case-insensitive match)
- `!~` (not regex match)
- `!~*` (not regex case-insensitive match)

Logical operators

- AND
- OR

Bitwise operators

- `&` (bitwise and)
- `|` (bitwise or)
- `#` (bitwise xor)
- `>>` (bitwise shift right)
- `<<` (bitwise shift left)

Other operators

- `||` (string concatenation)
- `@>` (array contains)
- `<@` (array is contained by)

* * *

### Aggregate functions

General

- avg
- bit\_and
- bit\_or
- bit\_xor
- bool\_and
- bool\_or
- count
- max
- mean
- median
- min
- sum
- array\_agg
- first\_value
- last\_value

Statistical

- corr
- covar
- covar\_pop
- covar\_samp
- stddev
- stddev\_pop
- stddev\_samp
- var
- var\_pop
- var\_samp
- regr\_avgx
- regr\_avgy
- regr\_count
- regr\_intercept
- regr\_r2
- regr\_slope
- regr\_sxx
- regr\_syy
- regr\_sxy

Approximate

- approx\_distinct
- approx\_median
- approx\_percentile\_cont
- approx\_percentile\_cont\_with\_weight

* * *

### Window functions

Aggregate functions

All [aggregate functions](/en/features/sql-transformations-query-setting#aggregate-functions-supported) can be used as window functions.

Ranking functions

- row\_number
- rank
- dense\_rank
- ntile

Analytical functions

- cume\_dist
- percent\_rank
- lag
- lead
- first\_value
- last\_value
- nth\_value

* * *

### Scalar functions

Math functions

- abs(x)
- acos(x)
- acosh(x)
- asin(x)
- asinh(x)
- atan(x)
- atanh(x)
- atan2(y, x)
- cbrt(x)
- ceil(x)
- cos(x)
- cosh(x)
- degrees(x)
- exp(x)
- factorial(x)
- floor(x)
- gcd(x, y)
- isnan(x)
- iszero(x)
- lcm(x, y)
- ln(x)
- log(base, x)
- log10(x)
- log2(x)
- nanvl(x, y)
- pi()
- power(base, exponent)
- pow(base, exponent)
- radians(x)
- random()
- round(x\[, decimal\_places\])
- signum(x)
- sin(x)
- sinh(x)
- sqrt(x)
- tan(x)
- tanh(x)
- trunc(x\[, decimal\_places\])

Conditional functions

- coalesce
- nullif
- nvl
- nvl2
- ifnull

String functions

- ascii
- bit\_length
- btrim
- char\_length
- character\_length
- concat
- concat\_ws
- chr
- ends\_with
- initcap
- instr
- left
- length
- lower
- lpad
- ltrim
- octet\_length
- repeat
- replace
- reverse
- right
- rpad
- rtrim
- split\_part
- starts\_with
- strpos
- substr
- to\_hex
- translate
- trim
- upper
- uuid
- overlay
- levenshtein
- substr\_index
- find\_in\_set
- position
- contains

Binary string functions

- decode
- encode

Regular expression functions

- regexp\_like
- regexp\_match
- regexp\_replace

Temporal functions

- now
- current\_date
- current\_time
- date\_bin
- date\_trunc
- datetrunc
- date\_part
- datepart
- extract
- today
- make\_date
- to\_char(expression, format)
  - Example: to\_char("Date", "%Y-%m-%d")
- to\_date
- to\_local\_time
- to\_timestamp
- to\_timestamp\_millis
- to\_timestamp\_micros
- to\_timestamp\_nanos
- to\_timestamp\_seconds
- from\_unixtime

Array functions

- array\_append
- array\_sort
- array\_cat
- array\_concat
- array\_contains
- array\_dims
- array\_distinct
- array\_has
- array\_has\_all
- array\_has\_any
- array\_element
- array\_empty
- array\_except
- array\_extract
- array\_fill
- array\_indexof
- array\_intersect
- array\_join
- array\_length
- array\_ndims
- array\_prepend
- array\_pop\_front
- array\_pop\_back
- array\_position
- array\_positions
- array\_push\_back
- array\_push\_front
- array\_repeat
- array\_resize
- array\_remove
- array\_remove\_n
- array\_remove\_all
- array\_replace
- array\_replace\_n
- array\_replace\_all
- array\_reverse
- array\_slice
- array\_to\_string
- array\_union
- cardinality
- empty
- flatten
- generate\_series
- list\_append
- list\_sort
- list\_cat
- list\_concat
- list\_dims
- list\_distinct
- list\_element
- list\_except
- list\_extract
- list\_has
- list\_has\_all
- list\_has\_any
- list\_indexof
- list\_intersect
- list\_join
- list\_length
- list\_ndims
- list\_prepend
- list\_pop\_back
- list\_pop\_front
- list\_position
- list\_positions
- list\_push\_back
- list\_push\_front
- list\_repeat
- list\_resize
- list\_remove
- list\_remove\_n
- list\_remove\_all
- list\_replace
- list\_replace\_n
- list\_replace\_all
- list\_slice
- list\_to\_string
- list\_union
- make\_array
- make\_list
- string\_to\_array
- string\_to\_list
- trim\_array
- unnest
- range

Struct functions

- struct
- named\_struct
- unnest

Hashing functions

- digest
- md5
- sha224
- sha256
- sha384
- sha512

Other functions

- arrow\_cast
- arrow\_typeof

* * *

## Read next

1. [Configure your output](/en/features/sql-transformations-output-setting)
2. [Output fields](/en/features/sql-transformations-output-fields)

> **SAMPLE USE CASES**
> 
> See our guides for step-by-step instructions on how to leverage SQL Transformations for the following use cases:
> 
> - [Change data capture](/en/features/sql-transformations-cdc)
> - [Data validation and cleansing](/en/features/sql-transformations-data-validation-cleansing)
> - [Data enrichment](/en/features/sql-transformations-data-enrichment)

---

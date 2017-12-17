# Nested Print
A lightweight nested printing, for all your function within loops within function needs

## Installation
You can install using pip with

```bash
    pip3 install --user nested_print
```

## Usage
This functions like an extension to the python print API, so you can use `end` and `sep` and everything else listed in the [print API](https://docs.python.org/3/library/functions.html#print). Only additional fields are added:

* level
* nest

### Basic Example

```python
from nested_print import nprint

nprint("hi", "there", level=2)              # returns \t\t hi there
nprint("hi", "there", level=1, nest="--")   # returns -- hi there
```

### Motivation Example

```python
from nested_print import nprint

nprint("here")
for i in range(10):
    nprint(i, level=1)
    for j in range(3):
        nprint(j, level=2)
```

### API

#### level
This describes how many "nest" or "indentations" to add. Setting `level=0` is the same as using print. `level=1` indents the output once, such that a `\t` is added in front when printing.

#### nest
By default, nest is set to `\t`. This value can be set if you want to modify the indentation. For example, instead of using `\t`, you can set `nest="  "` to just add 2 spaces as the indentation. Or set `nest="--"` to set two dashes for every indentation.

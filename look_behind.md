# Lookbehind assertion

- a lookbehind assertion "looks behind" the current cursor position
- attempts matching the previous input with the given pattern
- it does not consume any of the input
- lookbehind asserts what is on the left
- there is also lookahead which asserts what is on the right
- regular expression matches backwards

## Syntax 
- (?<=pattern) success means `pattern` must match the input immediately to the left of the current posiiton
- (?<!pattern) this is the negative form - it succeeds if the `pattern` does not match immediately to the left of current position

## Example
- Find expression A where expression B follows: `(?<=B)A` | positive
- Find expression A where expression B does not follow `(?<!B)A` | negative



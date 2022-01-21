# pyhl7

Toy Hl7 message parser. It has potential! Don't even think about using it for anything not fun.

## Usage

1. `import pyhl7.Hl7 as Hl7`
2. `hl7_object = Hl7.parse_file(<file>)`
3. `component = hl7_object.get(<segment>, idx=<idx; default 0>).get(<component_idx>, <optional_subcomponent_idx>)`
4. Every hl7 class has a string representation. Getting a subcomponent returns its value

## Caveats

- For now, 0 index is the item after the segment head (MSH, PIV, etc). I believe this is in contrast to the Java HAPI libs starting at 1.
- Standard separators \n|^ apply only

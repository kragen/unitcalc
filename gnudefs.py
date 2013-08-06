"""
Parse definitions.units
"""

import re
from unitcalc import calc, standard_units

lines = open('definitions.units').read().splitlines()
lines = lines[:5174]   # unicode troubles after this
i = 0
while i < len(lines):
    if lines[i].endswith('\\'):
        lines[i] = lines[i][:-1] + lines[i+1]
        del lines[i+1]
    else:
        i += 1

def ok():
    for line in lines:
        if line[:1].isalpha() or line[:1] == '%':
            if '!' in line.split() or '!dimensionless' in line.split():
                continue
            line = re.sub(r'#.*', '', line)
            subject, definition = line.split(None, 1)
            if any(ch in "()[],.'" for ch in subject):
                continue
            if "'" in definition:
                continue
            print subject, definition
            standard_units[subject] = calc(definition)
            print '  ', standard_units[subject]
            if subject != 'in' and not subject.endswith('-') and subject+'s' not in standard_units:
                # XXX horrible hack
                standard_units[subject+'s'] = calc(subject)
#        print line
### ok()

## calc('(1)')
#. 1

## calc('5/6')
#. 0.8333333333333334
## calc('5 / ( 1 + 6)')
#. 0.7142857142857143
# Polar
Very Forgiving Interpreted Language
Created with Python: https://www.python.org/

Edited With Sublime Text 3 : https://www.sublimetext.com/

To Interperate A .plr Sript, You will need:

python: https://www.python.org **AND** The .plr interpreter https://github.com/INeedMenta1Help/Polar


- Navigate to where the file is saved using **Command Prompt** or your chosen shell that allows for the running of python scripts along with other files.
- Write: `py plr.py filename` and Hit Enter

## **The Aim Of Polar**
Polar is a **variable** orientated Language.

_What Does That Mean?_

Its just one big **Overcomplicated** Calculator! x3


Polar was created to be an easy way into programming, I designed the interpreter to be as forgiving as possible so that one small mistake does not completely break the entire program.

## **Updates**
### **14/11/2018**
First **Public** upload of Polar.

basic syntax:
Declaring Variables:
**&**_VariableName_ = _VariableContents_
A Variable can either be:
  - A String: "Hello, World"
  - Number: 10
  - Another Variable: **&**_VariableName_ _(However, When the original variable changes, this one stays the same.)_
  - Example:
```
&x = "Hewwo, World!"
&y = 10
&z = &x
```

Operations On Variables:
**&**_VariableName_ __(+, -, *, /)__ Are all the basic 4 operators you will be using when making **.plr** scripts

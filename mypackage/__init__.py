print("eu sunt package")

PACKAGE_VAR = 22

# dacă vrem să ridicăm la suprafață
# un submodul, îl importăm aici:

from . import submodule
# și acum va fi disponibil ca
# mypackage.submodule

# importurile pot fi relative (cu .)
# doar în interiorul unui package
from .submodule import WHATEVER

# sintaxa completă de importing

# 1) import un modul

import os
import datetime as dt
import os.path

# când import direct modulul,
# simbolurile definite în interiorul său
# sunt atributele modulului
os.getcwd()
dt.datetime
os.path.join("un path", "alt path")


# 2) import simboluri din interiorul unui modul

from os import path # acesta este sub-modul
from datetime import datetime # aceasta este o clasă
# apoi, alias-uri:
from datetime import datetime as dt
# și apoi, simboluri multiple:
from datetime import datetime, date, time, timedelta
# sau mai ordonat:
from datetime import (
    datetime,
    date,
    time,
    timedelta as delta,
    tzinfo as tz,
)

# 2.1) import toate simbolurile dintr-un modul
from datetime import *
from os.path import *
# ^^ în general vorbind nu vreți să faceți asta
#    ca să nu poluați local namespace


##### our own module
import mymodule
print(mymodule.MY_VAR)


##### our own package
import mypackage


# modulele sunt importate din prima locație
# găsită în `sys.path`
# pe care puteți să-l modificați din interiorul aplicației
# (în general nu este recomandat ca aplicația să facă manipulări de path)
#
# varianta recomandată: variabila de sistem
# (setată înainte să se pornească python-ul) numită PYTHONPATH.
# are forma PYTHONPATH=director1

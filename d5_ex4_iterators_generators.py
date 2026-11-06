def myfunc():
    print("» am intrat în funcție")
    yield "unu"
    print("» continui după primul yield")
    yield "doi"
    print("» continui după al doilea yield")
    yield "trei"
    print("» ies din funcție")

# acesta creează un "generator object"
myfunc()

# generatorul este un caz particular de iterator.
# iteratorul:

# 1. este suspendat în execuție
# 2. este iterabil
# 3. când este iterat, i se reia execuția
#    și este re-suspendată
#    la fiecare din valori dată înapoi
# 4. un `for` face next() continuu
#    până la raise StopIteration


def mksquares(iterable):
    for elem in iterable:
        yield elem ** 2

for idx, elem in enumerate(mksquares(range(100))):
    print(idx, elem, sep=" ::\t")
    if idx >= 10: break

# Exercițiu:
# citim setul de date "data/temp_sensor_data.csv"
# și calculăm mediile orare, returnând tuple
# de forma (hour, average).

# clasele date, time, datetime din modulul datetime
# au classmethod-ul .strptime()
# și instance method-ul .strftime()

# și au și
# classmethod .fromisoformat()
# instance method .isoformat()

import csv
import datetime as dt
from collections import defaultdict

from time import sleep

# 1. varianta brute-force
def temp_averages_bf(csvfile):
    everything = defaultdict(list)

    with open(csvfile) as f:
        reader = csv.reader(f)

        for tstamp, value in reader:
            #tstamp = dt.time.strptime('07:00:03', '%H:%M:%S')
            tstamp = dt.time.fromisoformat(tstamp)
            value = float(value)

            # pun totul în memorie
            everything[tstamp.hour].append(value)

    return [
        (hour, sum(values) / len(values))
        for hour, values in everything.items()
    ]

# 2. varianta streaming
def temp_averages(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)

        # în timp ce iterez
        # dacă s-a schimbat ora curentă,
        # fac yield average-ului orei trecute.

        # pentru a putea face asta
        # am nevoie să contorizez totalul curent
        # și numărul de items curente

        total = 0
        count = 0

        old_hour = None

        for tstamp, value in reader:
            tstamp = dt.time.fromisoformat(tstamp)
            value = float(value)

            if old_hour is not None and tstamp.hour != old_hour:
                yield (old_hour, total / count)

                # și reset
                total = 0
                count = 0

            total += value
            count += 1

            old_hour = tstamp.hour

        # there is one final value
        yield (old_hour, total / count)

for tup in temp_averages("data/temp_sensor_data.csv"):
    print(tup)

# 3. exact același lucru,
#    dar separăm încărcarea și normalizarea datelor

def read_temperatures(csvfile):
    """
    loads and reads the given file
    yielding tuples of (timestamp, value)
    """
    with open(csvfile) as f:
        reader = csv.reader(f)

        for tstamp, value in reader:
            tstamp = dt.time.fromisoformat(tstamp)
            value = float(value)

            yield tstamp, value

# alternately, using agenerator expression:
def read_temperatures(csvfile):
    """
    loads and reads the given file
    yielding tuples of (timestamp, value)
    """

    # note: returning a generator expression
    # cannot be done within a context manager

    f = open(csvfile)
    reader = csv.reader(f)

    return (
        (
            dt.time.fromisoformat(tstamp),
            float(value)
        )
        for tstamp, value in reader
    )


def compute_averages(iterable):
    total = 0
    count = 0

    old_hour = None

    for tstamp, value in iterable:
        if old_hour is not None and tstamp.hour != old_hour:
            yield (old_hour, total / count)

            # și reset
            total = 0
            count = 0

        total += value
        count += 1

        old_hour = tstamp.hour

    # there is one final value
    yield (old_hour, total / count)

for tup in compute_averages(
    read_temperatures("data/temp_sensor_data.csv")
):
    print(tup)


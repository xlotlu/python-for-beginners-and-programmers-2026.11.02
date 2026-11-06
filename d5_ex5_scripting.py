#!/usr/bin/python

# scop:
# un modul hibrid, ce expune funcții utile
# în timp ce este și executabil

import sys
import datetime as dt

def process(tspec):
    """
    processes a string in the form
    HH:MM:SS and returns a datetime.time object
    """
    # TODO:
    # deal with inputs like 1:00
    return dt.time.fromisoformat(tspec)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("timespec",
                        type=str,
                        help="Required time (HH:MM or HH:MM:SS)",
    )

    parser.add_argument("--payload",
                        type=str,
                        default=None,
                        help="Optional payload",
    )

    args = parser.parse_args()

    #print(f"Timespec: {args.timespec}")
    #print(f"Payload: {args.payload}")

    print(
        process(args.timespec)
    )


    """
        try:
            timespec = sys.argv[1]
        except IndexError:
            print("Usage error, try....", file=sys.stderr)
            sys.exit(1)

        print(
            process(timespec).hour
        )
    """

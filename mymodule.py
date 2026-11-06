MY_VAR = 15

# la import se execută
# all top-level code
print("sunt în mymodule")

def myfunc():
    pass

# când sunt modul de sine stătător
# nu merg importurile relative
# from . import mypackage

if __name__ == "__main__":
    # pattern folosit pentru a crea module hibrid
    # care se comportă și ca library din care se face import
    # și ca executabil.

    print("sunt top-level executable")
    print("i will do executable stuff")

    # P.S.: putem executa un modul cu
    # python -m module_name
    # altfel
    # python cale/către/module_name.py

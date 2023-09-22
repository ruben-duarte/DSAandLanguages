# Make a function lowercase that, given a string, returns the 
# string, except in all lowercase letters.
#
# >>>> lowercase("ARG")
# arg
# >>>> lowercase("TRINKET")
# trinket

def lowercase(string):
    return string.lower()

arg = lowercase("ARG")
print(arg)

new = lowercase("HELLO GUYS")
print(new)


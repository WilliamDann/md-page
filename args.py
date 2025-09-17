# basic cmd args module
from sys import argv

# turn buffer into stored value
#  no followup items == True (beacuse it's a flag)
#  one followup item == String (because it's a single value)
#  many followups    == Array (because there's a few values)
def packBuffer(buffer):
    l = len(buffer)
    if l == 0:
        return True
    if l == 1:
        return buffer[0]
    return buffer

# get a map version of cmd args
def getArgs():
    data   = {}
    buffer = []
    arg    = None

    for i in range(len(argv)):
        if argv[i].startswith("--"):
            if arg is not None:
                data[arg]   = packBuffer(buffer)

            buffer      = []
            arg         = argv[i][2:]
        elif argv[i].startswith("-"):
            if arg is not None:
                data[arg]   = packBuffer(buffer)

            buffer      = []
            arg         = argv[i][1:]
        else:
            buffer.append(argv[i])


    data[arg] = packBuffer(buffer)
    return data

import config

# pring with an ANSI color code and reset code
def printRGB(text, r, g, b):
    print(f"\x1B[38;2;{r};{g};{b}m{text}\033[0m")

# print app header
def header():
    # print("\033[H\033[2J", end="") # clear term
    print(f"\x1B[38;2;150;50;255m{config.HEADER_TEXT}")
    print("\t\t\t\t\t\tmarkdown pages -> html")
    print("\t\t\t\t\t\t\twilliam dann")
    print("\033[0m")

# clear terminal
def clear():
    print("\033[H\033[2J", end="") # clear term
    header()


import sys
import os

import args
import cmd
import term
import config

# app setup
def init():
    # init steps
    config.ARGS = config.ARGS | args.getArgs()

    if config.HEADER_TEXT is None:
        with open("title.md") as f:
            config.HEADER_TEXT = f.read()

    if config.HTML_TEMPLATE is None:
        with open(os.path.join(config.ARGS['output'], 'template.html')) as f:
            config.HTML_TEMPLATE = f.read()

# app loop
def loop():
    val = input("> ")
    if val not in cmd.commands:
        term.printRGB(" ! unknown command", 255, 0, 0)
        loop()

    cmd.commands[val]()
    loop()

# main func
if __name__ == "__main__":
    init() 
    term.clear()
    loop()

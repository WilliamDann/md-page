import term
import md
import config
import watch

def done():
    quit()

def status():
    print(config.ARGS)
def compile():
    md.processDir(config.ARGS['input'], config.ARGS['output'])

# commands
commands = {
    "q"         : done,
    "quit"      : done,

    "c"         : term.clear,
    "clear"     : term.clear,

    "status"    : status,
    
    "c"         : compile,
    "compile"   : compile,

    "w"         : watch.watch,
    "watch"     : watch.watch,
}

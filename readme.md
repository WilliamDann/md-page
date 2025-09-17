# md-page
```
 __    __     _____        ______   ______     ______     ______    
/\ "-./  \   /\  __-.     /\  == \ /\  __ \   /\  ___\   /\  ___\   
\ \ \-./\ \  \ \ \/\ \    \ \  _-/ \ \  __ \  \ \ \__ \  \ \  __\   
 \ \_\ \ \_\  \ \____-     \ \_\    \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/  \/_/   \/____/      \/_/     \/_/\/_/   \/_____/   \/_____/ 
                                                                    
```

md-page is a tool to take markdown files and turn them into basic static webpages. I am using this for my own personal webpage.

## Args

| Command | Args         | Desc |
| ------- | ------------ | ---- |
| debug   | -            | if present app will be in debug mode
| input   | path/to/dir  | path app pulls markdown files from
| output  | path/to/dir  | path app outputs html files to

for example, to run in debug mode:
```
python3 mdpage.py --debug 
```
or to chage input dir
```
python3 mdpage.py --input path/to/input/dir/
```

## Commands
These commands are run in the program loop, once the app is started.

| Command | Args         | Desc |
| ------- | ------------ | ---- |
| quit    | -            | quits the app
| clear   | -            | clears the terminal
| status  | -            | gets status of app
| compile | -            | runs the compilation process once
| watch   | -            | runs the compilation process every time a file is changed

import markdown
import os
import config

# get file content, or None if fail
def getFile(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ""

# write html file
def writeHTML(path, html):
    text = config.HTML_TEMPLATE.replace("{content}", html)
    with open(path, 'w') as f:
        f.write(text)

# process an HTML file into an HTML file
def processFile(input_dir, output_dir, path):
    print(path)
    mdText = getFile(os.path.join(input_dir, path))
    html   = markdown.markdown(mdText, extensions=['tables'])
    writeHTML(os.path.join(output_dir, path.replace('.md', '.html')), html)

# process a directory of files
def processDir(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
               processFile(input_dir, output_dir, file) 

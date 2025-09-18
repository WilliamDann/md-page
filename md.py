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
    rel_path = os.path.relpath(path, input_dir)
    out_path = os.path.join(output_dir, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    md_text = getFile(path)
    html    = markdown.markdown(md_text, extensions=['tables'])
    writeHTML(out_path.replace('.md', '.html'), html)

# process a directory of files
def processDir(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if ".md" not in file:
                continue
            print(file)
            processFile(input_dir, output_dir, os.path.join(root, file))

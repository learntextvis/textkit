#!/usr/bin/env python

import sys
import os
import subprocess


def create_docs(command, path):
    proc = subprocess.Popen(["textkit", command, "--help"], stdout=subprocess.PIPE)
    out = str(proc.communicate()[0]).split('\\n')
    # print(out)
    content = "=" * len(command) + "\n"
    content += command + "\n"
    content += "=" * len(command) + "\n"

    content += "\n"
    content += "Description\n"
    content += "=" * len("Description") + "\n"
    content += "\n"
    content += "::\n"
    content += "\n"
    for line in out:
        content += "    " + line.replace("b'", '').replace("'", '') + "\n"
    content += "\n"
    content += "\n"
    content += "Examples\n"
    content += "=" * len("Examples") + "\n"
    print(content)

proc = subprocess.Popen(["textkit", "--help"], stdout=subprocess.PIPE)
out = str(proc.communicate()[0]).split('\\n')

commands = []

at_commands = False
for line in out:
    if at_commands:
        command = line.split()[0]
        if(len(command) > 3):
            commands.append(command)
    else:
        if "Commands:" in line:
            at_commands = True


print(commands)


path = os.path.dirname(os.path.realpath(__file__))
doc_path = os.path.join(path, "scripts")
print(doc_path)

for command in commands:
    command_doc_path = os.path.join(doc_path, command + ".rst")
    if not os.path.isfile(command_doc_path):
        print('creating: ' + command_doc_path)
        create_docs(command, command_doc_path)
        break
    else:
        print('skipping: ' + command_doc_path)

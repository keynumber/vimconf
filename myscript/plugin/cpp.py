function! GenSwitchCase() range

python << EOF

import vim

buffer = vim.current.buffer 
def GetItems(firstline, lastline):
    items = []
    idx = firstline
    while (idx < lastline):
        items = items + buffer[idx].split()
        idx = idx + 1
    return items

def GenSwitchCase(item_list, prefix):
    lines = [prefix + "switch () {"]
    for item in item_list:
        lines.append(prefix + "case " + item + ":")
        lines.append(prefix + "{")
        lines.append(prefix + "    break;")
        lines.append(prefix + "}")

    lines.append(prefix + "default:")
    lines.append(prefix + "{")
    lines.append(prefix + "    break;")
    lines.append(prefix + "}")
    lines.append(prefix + "}")
    return lines

firstline = int(vim.eval("a:firstline")) - 1
lastline= int(vim.eval("a:lastline"))

tabstop = int(vim.eval("&tabstop"))
space_num = 0
for i in buffer[firstline]:
    if (i == ' '):
        space_num = space_num + 1
    elif (i == '\t'):
        space_num += tabstop
    else:
        break

prefix = " " * space_num

item_list = GetItems(firstline, lastline)
lines = GenSwitchCase(item_list, prefix)
del buffer[firstline:lastline]
buffer.append(lines, firstline)
vim.current.window.cursor = (firstline+1, 0)
vim.command("normal f(")


EOF

endfunction

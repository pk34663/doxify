import vim
import re

function = re.compile("^.* ([^(].*)\(")
arguments = re.compile("^.*\(([^)].*)\)")

doxy = ["/**"," *"]

buffer = vim.current.buffer
(row,_) = vim.current.window.cursor
line = vim.current.line
row = row - 1
start = row
while "{" not in line:
  row = row + 1
  line += buffer[row]

func = function.match(line)
args = arguments.match(line)

if func.group(1) != None:
  doxy.append(" * @brief " + func.group(1))
else:
  doxy.append(" * @brief")

if args.group(1) != None:
  doxy.append(" * @param " + args.group(1))
else:
  doxy.append(" * @param")

doxy.append(" */")
buffer.append(doxy, start)

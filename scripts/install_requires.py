# -*- coding: utf-8 -*-
import os, jmp, jmputils

require_file = os.path.join(gdd, ".requirements.txt")

with open(require_file, "w", encoding = "utf-8") as rfw:
    rfw.write(reqList.strip())

try:
    jmputils.jpip(f'install -r {require_file}')
    os.remove(require_file)
    
    jmp.run_jsl('tbRequireProgress << SetText("Installed!");')
except:
    jmp.run_jsl('tbRequireProgress << SetText("Error!");')

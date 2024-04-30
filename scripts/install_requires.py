# -*- coding: utf-8 -*-
import os, jmp, jmputils


if useFile:
	try:
		jmputils.jpip(f'install -r "{reqFile}"')
		jmp.run_jsl('tbRequireProgress << SetText("Installed!");')
	except:
		jmp.run_jsl('tbRequireProgress << SetText("Error!");')
else:
	require_file = os.path.join(gdd, "requirements.txt")

	with open(require_file, "w", encoding = "utf-8") as rfw:
		rfw.write(reqList)

	try:
		jmputils.jpip(f'install -r {require_file}')
		os.remove(require_file)
		
		jmp.run_jsl('tbRequireProgress << SetText("Installed!");')
	except:
		jmp.run_jsl('tbRequireProgress << SetText("Error!");')

# -*- coding: utf-8 -*-
import os, sys, jmp, pathlib, subprocess


# get jmp and user home path
python_path = pathlib.Path(jmp.PYTHON_EXE).resolve()
user_home_dir = pathlib.Path(os.path.expanduser("~")).resolve()

# find python, jsite file path and PYTHONUSERBASE
if sys.platform == "darwin":
	jsite_file = str(python_path.parent.joinpath("jsite.py"))
	python_userbase = user_home_dir.joinpath("Library", "Application Support", "JMP", "Python", "3.11")
else:
	jsite_file = str(python_path.parent.joinpath("jsite.py"))
	python_userbase = user_home_dir.joinpath("AppData", "Roaming", "JMP", "JMP", "Python")

# run jsite.py
jmp.run_jsl('tbProcess << SetText("Running `jsite.py`...");')
subprocess.call([ str(python_path), jsite_file ], env = { "PYTHONUSERBASE": str(python_userbase) })
jmp.run_jsl('tbProcess << SetText("`jsite.py` Complete!");')

# copy python as jmp_python and append to path(if MAC)
if sys.platform == "darwin":
	jmp.run_jsl('tbProcess << SetText("Set Environment...(MAC only)");')
	python_userbase_bin = python_userbase.joinpath("bin")
	if not python_userbase_bin.exists():
		os.mkdir(str(python_userbase_bin))

		os.symlink(str(python_path), str(python_userbase_bin.joinpath("jmp_python")))
		
		with open(str(user_home_dir.joinpath(".zshrc")), "a", encoding = "utf-8") as vfw:
			vfw.write(f"""# JMP
export PYTHONUSERBASE="{python_userbase}"
export PATH="{python_userbase_bin}:$PATH"
""")
	jmp.run_jsl('tbProcess << SetText("Set Environment Complete!");')

jmp.run_jsl("""
tbProcess << SetText("Finished!");
btnStart << Visibility("Collapse");
btnClose << Visibility("Visible");
""")

# -*- coding: utf-8 -*-
import os, sys, jmp, pathlib, subprocess, shutil


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

# post setup(environment variable, copy dt2pandas.py)
if sys.platform == "darwin":
    # copy python as jmp_python and append to path(if MAC)
    jmp.run_jsl('tbProcess << SetText("Set Environment...(MAC only)");')
    python_userbase_bin = python_userbase.joinpath("bin")
    if not python_userbase_bin.exists():
        os.makedirs(str(python_userbase_bin))

        os.symlink(str(python_path), str(python_userbase_bin.joinpath("jmp_python")))
        
        with open(str(user_home_dir.joinpath(".zshrc")), "a", encoding = "utf-8") as vfw:
            vfw.write(f"""# JMP
    export PYTHONUSERBASE="{python_userbase}"
    export PATH="{python_userbase_bin}:$PATH"
    """)
    jmp.run_jsl('tbProcess << SetText("Set Environment Complete!");')

    shutil.copyfile(os.path.join(jmp.SAMPLE_SCRIPTS, "Python", "dt2pandas.py"), str(python_userbase.joinpath("lib", "python", "site-packages", "dt2pandas.py")))
else:
    # register environment
    os.system(f'setx PYTHONUSERBASE="{python_userbase}"')
    os.system(f'setx PATH="%PATH%;{python_path.parent}"')

    shutil.copyfile(os.path.join(jmp.SAMPLE_SCRIPTS, "Python", "dt2pandas.py"), str(python_userbase.joinpath("Python311", "site-packages", "dt2pandas.py")))

jmp.run_jsl("""
tbProcess << SetText("Finished!");
tb << SetSelected(2);
""")

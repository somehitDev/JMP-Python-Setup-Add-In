## 2024.04.30
- first release

## 2024.05.03
- add "README.md" and "CHANGELOG.md"
- change python path to jmp.PYTHON_EXE(not find path by sys.executable)
- hide menubar and toolbar from window
- fix auto resizing when check/uncheck require file
- scriptbox now hide normally

## 2024.07.25
- fix bug from `setup.py` file.

## 2024.11.13
- change ui.
  - `Setup` page
    - remove `Close` button.
    - align horizontally center all elements.
  - `Requirements` page
    - align vertically center progress TextBox.
    - remove `use file` checkbox and file selector.
    - add `Load File...` button.
      - if select by this button, replace content of ScriptBox to contents of requirements file.
- add `load_require_file.py`.
- fix `setup.py`, `install_requires.py` according to changes of ui.
- replace images by above.

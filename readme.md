# FiveM to Single Player format

<center style="margin-bottom: 30px;">
    by <b>belicfr</b>
</center>

This simple Python script allows you to convert a FiveM add-on setup to a Single Player one. It uses the `os` and `shutil` libraries to get an optimized source code.

## Get started
Let's install this simple script! Before use it, you must install Python language. The `os` and `shutil` libraries may be included with Python.

Then, put your **FiveM** files (`my^path^to^file.ydd` for example) in `fivem_format` folder.

When these two steps are done, let's start the script using command-line like Windows CMD.

## And the result?
You can find the convertion result in `sp_format` folder.

## `os` library?
This library allows us to navigate around our files. In the source code, it is used to navigate in the FiveM / SP internal paths on script folder (`fivem_format` and `sp_format` folders).

## `shutil` library?
This library is used to copy files without read they. Useful to copy bin files like `.ytd` and `.ydd` files.
from cx_Freeze import setup,Executable
setup(
    name="Monprog",
    version="0.1",
	description="Classifer",
	executables=[Executable("test.py")]
	)
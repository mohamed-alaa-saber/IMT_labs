import subprocess


#give path open location
path=input() #for example D:\IMT\Data\LEC
subprocess.Popen(r"explorer /select,{}".format(path))

import  os
pwd = os.getcwd()
print(pwd)
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
print(father_path)
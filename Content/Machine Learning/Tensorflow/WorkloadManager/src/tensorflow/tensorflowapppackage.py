import requests
import os
import shutil
import subprocess,sys
import zipfile,platform
from util import print_log, print_error, print_result

InitFile=os.environ['InitFile']
InitFile='/opt'+"/"+InitFile
TensorboardLogpath=os.environ['TensorboardLogpath']
try:
    downloadpath= r"/opt/remoteFiles/DatasetsURL"
    target_path=os.listdir(downloadpath)[0]
    path='/opt'
    retcode = subprocess.call(['tar', '-xvf',downloadpath+"/"+target_path, '-C', path])
    print_log("Datasets Extracted successfully")
    target_path=target_path.split(".tar.gz")[0]
    print(target_path)
    retcode = subprocess.call(['mv', "/opt/"+target_path, '/opt/datasetsmodel/'])
    os.chmod("/opt/datasetsmodel",755)
except Exception as e:
    print(e)
    print("Error while configuring datasets folder")
    print_error(e)
    write_error(e)
    print_error("Error while configuring datasets folder")
    sys.exit(127)
#download and configuring package file
try:
    downloadpath= r"/opt/remoteFiles/PythonPackage"
    target_path=os.listdir(downloadpath)[0]
    with zipfile.ZipFile(downloadpath+"/"+target_path, "r") as zip_ref:
        zip_ref.extractall("/opt")
    target_path = target_path.split(".zip")[0]
    print("calling and installing requirements.txt")
    os_find = platform.linux_distribution()
    if "Ubuntu" in os_find[0]:
        print ("In ubuntu")
        retcode = subprocess.call (['python', '-m', 'pip', 'install', "-r", "/opt/requirements.txt"])
        print_log("Requirements.txt intialized.")
    elif "CentOS" in os_find[0]:
        retcode = subprocess.call (['pip', 'install', "-r", "/opt/requirements.txt"])
        print_log("Requirements.txt intialized.")
    tensorboardpath = TensorboardLogpath
    os.mkdir("/opt/tensorflow")
    os.system("nohup python %s > /dev/null 2>&1 &"%(InitFile))
    if tensorboardpath:
        retcode = os.system('nohup tensorboard --logdir=%s --host=0.0.0.0 --port=8080 > /dev/null 2>&1 & '%(tensorboardpath))
except Exception as e:
    print(e)
    print("Error while configuring python package..")
    print_error(e)
    write_error(e)
    print_error("Error while configuring python package..")
    sys.exit(127)











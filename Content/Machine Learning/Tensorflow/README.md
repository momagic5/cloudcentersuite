# Tensorflow
## Introduction
    TensorFlow is an open source library for numerical computation and large-scale machine learning. 
    TensorFlow bundles together a slew of machine learning and deep learning (aka neural networking) 
    models and algorithms and makes them useful by way of a common metaphor..  
    
    Please refer the below link for more details.
    https://www.tensorflow.org/
## Pre-Requisites
#### CloudCenter
- CloudCenter 5.0.1 and above
- Knowledge on how to use Workload Manager
- Supported OS: CentOS 7 , Ubuntu 16

#### Before you start
Before you start with service import, Install Docker by following the steps provided [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/dockerimages/Steps%20for%20Installation%20of%20Docker%20CE%20on%20CentOS7_V2.docx), on any linux based client machine.

**NOTE** : You can skip the above step, if Docker Client is already installed and running in your machine. 
- You can check , if docker is installed , by running "docker -v"
- You can check , if docker is running , by executing the command "systemctl status docker"

## Importing the service
Step 1 : Download the service import utility file  from [here](https://raw.githubusercontent.com/datacenter/cloudcentersuite/master/Content/Scripts/ServiceImportMaster.sh), and save the file on to your linux machine.
- wget command may not be installed. Need to execute "yum install wget -y" in case of centos7.

	    Example: 
      wget https://github.com/datacenter/cloudcentersuite/raw/master/Content/Scripts/ServiceImportMaster.sh
				
- After downloading ServiceImportMaster.sh, provide file permissions by executing "chmod 755 ServiceImportMaster.sh".

Step 2 : Execute the script from Step 1 using the following command.

        sh ServiceImportMaster.sh

Once the script is run, please follow the prompts to import the service or the corresponding application profile.

##### PLEASE NOTE : You be prompted with location of service bundle zip, application bundle zip on client machine. The files must be copied on to the repository before proceeding to deploy.

         - Service Zip file under <service_path>/<your_bundle_name>
                    
             Example : http://<Your_REPO_Server_IP>/<service_path>/tensorflow.zip 
    
         - Application Zip file under <app_path>/<your_package_name>
            
             Example: http://<Your_REPO_Server_IP>/<app_path>/objectdetection.zip

## Service Package Bundle

The Packer Service bundle consists of the following files:

Shell script:
 - service: The script will set all required environmental variables and installs necessary packages also invokes all external life cycle action.
Python File:
 - tensorflowapppackage.py: This script will invoke the init file provided by the user and download the datasets and models required as well.
 
## Agent Lifecycle Actions

Agent Actions Bundle:  
 - http://<Your_REPO_Server_IP>/services/tensorflow.zip.
 
External Lifecycle Actions:
 - Deploy: Script from bundle: **service install**
 - Stop: Script from bundle: **service stop**
 
 ## Deployment parameters


| Parameter Name	| Type	 | Description | Allowed Value |Default Value |
| ------ | ------ | ------ |------ | ------ |
| PythonPackage  |	path | Package of your tensorflow model . | | |
| InitFile | string|Tensorflow model initialization (.py)File  |  |  |
| Tensorboard log directory path | string| Path of the log file for tensorboard |  |  |
| DatasetsURL | path|Path of the Tensorflow Datasets |  |  |

**NOTE** : 
    PythonPackage : It should contain 
        - Trained tensorflow model files in 'model' directory
        - Requirements.txt(to install pre-requisites of importable modules)(Mandatory) 
    
      Example: http://<REPO-IP>/apps/objectdetection.zip
    
   DatasetsURL   : Trained datasets repository URL (GitHub or Local repository). The file should enclosed in tar.gz . 
     To access your given datasets in your python code of tensorflow model the path is "/opt/datasetsmodel"  
            
      
      Example: http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz
      Example: datasets="/opt/datasetsmodel/imagerecognition.pb"
     
   
# Minimum Resource Specifications

     
S.No    | Resource    |  Value   | Remarks
----    | ----------  | ---------| ------- 
 1      |  CPU        | 2       |        
 2      |  Memory     | 8 GB     | 		


**NOTE** : For demo we have used flask application for Image recoginition.
   To access the application please refer the credentials below .
   Username : username
   Password : passw0rd
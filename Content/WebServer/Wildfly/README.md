
# WildFly

## Introduction

    The Workload Manager platform supports integration to various Webservers.

    This document provides information on WildFly integration with Cisco Workload Manager by creating a 
    Virtual Machine (VM) with Agent service .

    WildFly is a open source Web Server which gives you the ability to deploy Java/J2EE Web applications.
	
	WildFly Application Server is configured in Port 8080, and administrator console will work on default Port 9990.
	
    Please refer the below link for more details.

    https://docs.wildfly.org/16/

## Pre-Requisites
#### CloudCenter
- CloudCenter 5.x.x and above
- Knowledge on how to use Workload Manager
- Supported OS: CentOS/Ubuntu
- Supported clouds: Google and Azure.


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

Once the script is run, please follow the prompts to import the service or the correspondong application profile.


##### PLEASE NOTE : You will be prompted with location of service bundle zip and/or application bundle zip on client machine. The files must be copied on to the repository before proceeding to deploy.

        - Service Bundle under <service_path>/<your_bundle_name>
                    
                    Example : http://<Your_REPO_Server_IP>/<service_path>/wildfly.zip 
    
        - Application Bundle under <app_path>/<your_package_name>	
            
                    Example : http://<Your_REPO_Server_IP>/<app_path>/wildfly-petclinic-app.zip

## Service Package Bundle

The Package Service bundle consists of the following files:

Shell script:

- service: This script will set all required environment variables, install necessary packages and also invokes the Agent life cycle actions.

## Minimum Resource Specifications

S.No | Resource   |  Value   | Remarks
---- | ---------- |--------- | ------- 
 1   |  CPU       | 1        |        
 2   |  Memory    | 1GB      |        

## Agent Lifecycle Actions 

Agent Action Bundle: 
 - http://YourIP/services/wildfly.zip - Location where your agent action bundle zip (service bundle zip file) is found.
 
Agent Lifecycle Actions:
 - install: Script from bundle: **service install**
 - deploy: Script from bundle: **service deploy**
 - configure: Script from bundle: **service configure** 
 - start: Script from bundle: **service start**
 - stop: Script from bundle: **service stop**
 - restart: Script from bundle: **service restart** 


## Service parameters


| Parameter Name	| Type	 | Description | Allowed Value |Default Value |
| ------ | ------ | ------ |------ | ------ |
| wlfyJDKVersion |	list | App Run-time | JDK8 | JDK8 |
| wlfyWarFile | path| Path of the Deployment Package(.zip).	 | User Defined Value | - |
| wlfyAppConfigFiles | string| App Config files |User Defined Value | - |
| wlfyAppContextName | string| Application Context Name | User Defined Value | - |
| wlfyAdminUsername | string| Admin Console Username | rootadmin | rootadmin |
| wlfyAdminPwd | string| Admin Console Password | admin@123 | admin@123 | 



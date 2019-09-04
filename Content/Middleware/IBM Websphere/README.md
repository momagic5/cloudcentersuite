# IBM WebSphere
## Introduction
    WebSphere Application Server (WAS) is a software product that 
	performs the role of a web application server. 
	
	More specifically, it is a software framework and middleware 
	that hosts Java-based web applications. 
	It is the flagship product within IBM's WebSphere software suite. 

    Please refer the below link for more details.
   https://www.ibm.com/cloud/websphere-application-platform
 
## Pre-Requisites
  - IBM Installation Manager zip file is mandatory to run websphere, Please make it available, by downloading the same from its website. For further details please refer [here](https://www-945.ibm.com/support/fixcentral). 
  - Prepare the response file to install the required websphere application server(was) packages using ibm installation manager.
  - Requires IBM Software Website login credentials to continue installation.
  
#### CloudCenter
 - CloudCenter 5.x.x and above
 - Knowledge on how to use Workload Manager 
 - Supported OS: CentOS 7, Ubuntu 16.04

#### Before you start
Before you start with service import, Install Docker by following the steps provided [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/dockerimages/Steps%20for%20Installation%20of%20Docker%20CE%20on%20CentOS7_V2.docx), on any linux based client machine.

**NOTE** : You can skip the above step, if Docker Client is already installed and running in your machine. 
- You can check , if docker is installed , by running "docker -v"
- You can check , if docker is running , by executing the command "systemctl status docker"

Also, Put the downloaded ibm installation zip file and the response file into http repository.

## Importing the service

Step 1 : Download the service import utility file  from [here](https://raw.githubusercontent.com/datacenter/cloudcentersuite/master/Content/Scripts/ServiceImportMaster.sh), and save the file on to your linux machine.
- wget command may not be installed. Need to execute "yum install wget -y" in case of centos7.

	    Example: 
      wget https://github.com/datacenter/cloudcentersuite/raw/master/Content/Scripts/ServiceImportMaster.sh
				
- After downloading ServiceImportMaster.sh, provide file permissions by executing "chmod 755 ServiceImportMaster.sh".
				

Step 2 : Execute the script from Step 1 using the following command.

        sh ServiceImportMaster.sh

Once the script is run, please follow the prompts to import the service or the corresponding application profile.

##### PLEASE NOTE : You will be prompted with location of service bundle zip, application bundle zip on client machine. The files must be copied on to the repository before proceeding to deploy.

    - Service Bundle under <service_path>/<bundle.zip>
                    
               Example : http://<Your_REPO_Server_IP>/<service_path>/websphere.zip 
    
    - Application Bundle under <app_path>/<your_package_name>
		- Please keep all individual artifacts files in apps folder, like below
            
               Example : http://<Your_REPO_Server_IP>/<app_path>/petclinic.war
			   Example : http://<Your_REPO_Server_IP>/<app_path>/websphere_dbinit.sql
			   Example : http://<Your_REPO_Server_IP>/<app_path>/websphere_mysqldb.sh
                

# Defaults
 - Application Profile has been configured with 2 Nodes

# Service Package Bundle

The Package of Service bundle consists of the following files:

Shell script:
 - service: This script will install the installation manager and install all required websphere application server packages and install necessary packages and also invokes the external life cycle actions.
 
Python file:
 - run.py: This script will create cluster and servers on each node and it will deploy the application on all servers.
 - start.py: This script will start the cluster, servers and applications.
 - stop.py: This script will stop the servers and its applications.
 - util.py: Utility file
 - wsadminlib.py: IBM open source helper utility file to use wsadmin scripting.

# Minimum Resource Specifications

S.No    | Resource     |  Value   | Remarks
----    | ----------   |--------- | ------- 
 1      |  4 CPU       | 8 GB     |        


# Agent Lifecycle Actions 
Agent Action Bundle:  
 - http://YourIP/services/websphere.zip - Location where your agent action bundle zip is found.

Agent Lifecycle Actions:
 - Install: Script from bundle: **service install**
 - Deploy: Script from bundle: **service deploy**
 - Configure: Script from bundle: **service configure**
 - Start: Script from bundle: **service start**
 - Stop: Script from bundle: **service stop**
 - Restart: Script from bundle: **service restart**


 # Service Parameters

| Parameter Name	| Type	 | Description | Allowed Value |Default Value |
| ------ | ------ | ------ |------ | ------ |
| websphereVersion | List | WebSphere Version | 9.0  | 9.0|  |
| appPackage |	Path |	 Application Package which is to be deployed on server  |  | | 
| appConfigFile | string  | Application configuration file  |
| applicationName | string | Application Name  | | |
| installerPath | path | Repository path where IBM WebSphere Agent zip file to install is available| | 
| adminUsername | string | Administrator Username  | | |
| adminPassword | string | Administrator Password | | |
| ibmUserName | string | IBM software website login Username  | | |
| ibmPassword | string | IBM software website login Password | | |
# Grafana Integration Unit

## Introduction

Grafana is an open source, feature rich metrics dashboard and graph editor for Mysql.

**Grafana** is an open source metric analytics &amp; visualization suite. It is most commonly **used** for visualizing time series data for infrastructure and application analytics but many **use** it in other domains including industrial sensors, home automation, weather, and process control.

Grafana ships with a built-in MySQL data source plugin that allow you to query any visualize data from a MySQL compatible database.

MySQL is the most popular Open Source Relational SQL Database Management System. MySQL is one of the best RDBMS being used for developing various web-based software applications

Please refer the below link for more details.

https://grafana.com/docs/features/datasources/mysql/

## Pre-Requisites

#### CloudCenter

- .CloudCenter 5.x.x and above
- .Knowledge on how to use Workload Manager
- .Supported OS: CentOS 7 , Ubuntu 16

#### Before you start

Before you start with service import, Install Docker by following the steps provided [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/dockerimages/Steps%20for%20Installation%20of%20Docker%20CE%20on%20CentOS7_V2.docx), on any linux based client machine.

**NOTE**  : You can skip the above step, if Docker Client is already installed and running in your machine.

- .You can check , if docker is installed , by running &quot;docker -v&quot;
- .You can check , if docker is running , by executing the command &quot;systemctl status docker&quot;

## Importing the service

Step 1 : Download the service import utility file from [here](https://raw.githubusercontent.com/datacenter/cloudcentersuite/master/Content/Scripts/ServiceImportMaster.sh), and save the file on to your linux machine.

- .wget command may not be installed. Need to add &quot;yum install wget -y&quot; in case of centos7.
- .  Example:
- .  wget [https://github.com/datacenter/cloudcentersuite/raw/master/Content/Scripts/ServiceImportMaster.sh](https://github.com/datacenter/cloudcentersuite/raw/master/Content/Scripts/ServiceImportMaster.sh)
- .After downloading ServiceImportMaster.sh, provide file permissions by executing &quot;chmod 755 ServiceImportMaster.sh&quot;.

Step 2 : Execute the script from Step 1 using the following command.

   sh ServiceImportMaster.sh

Once the script is run, please follow the prompts to import the service or the corresponding application profile.

##### PLEASE NOTE : You be prompted with location of service bundle zip and/or application bundle zip on client machine. The files must be copied on to the repository before proceeding to deploy.

    - Service Zip file under \&lt;service\_path\&gt;/\&lt;your\_bundle\_name\&gt;

         Example : http://\&lt;Your\_REPO\_Server\_IP\&gt;/\&lt;service\_path\&gt;/grafana.zip

## Service Package Bundle

The Package Service bundle consists of the following files:

Shell script:

- .service: This script will install grafana and installs necessary packages, loads configuration and also invokes the agent life cycle actions.

# Minimum Resource Specifications

| S.No | Resource | Value | Remarks |
| --- | --- | --- | --- |
| 1 | CPU | 1 |   |
| 2 | Memory | 2 GB |   |

## Agent Lifecycle Actions

Agent Action Bundle:

- .[http://YourIP/services/grafana.zip](http://YourIP/services/grafana.zip) - Location where your agent action bundle zip (service bundle zip file) is found.

Agent Lifecycle Actions:

- .Install: Script from bundle:  **service install**
- .Configure: Script from bundle:  **service configure**
- .Start: Script from bundle:  **service start**
- .Stop: Script from bundle:  **service stop**

Detailed Steps To Retrieve Data From Mysql To Grafana Dashboard

Step 1 : Deploy Grafana application.

Step 2 : In a web browser, go to the public IP address of your Grafana server. You will see the Grafana homepage.

          - [http://your\_server\_ip:3000/](http://your_server_ip:3000/)

Step 3 :   Click Create your first dashboard and  add a new graph by selecting a graph type.

Step 4: change the Format as type as a Table.

           select \* from yourtablename;
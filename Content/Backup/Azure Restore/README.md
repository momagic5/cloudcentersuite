# Azure Restore

   ## Introduction
   The Azure Restore will restore Azure Virtual Machines backup from Recovery Service Vault to new Virtual Machine or we can restore a 
   disk, and use it to replace a disk on the existing VM or restores a VM disk, which can then be used to create a new VM
   
   Please refer the below link for more details.
   
   For your reference : https://docs.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms
	
## Before you start
   Make sure that Recovery Service Vault and existing Azure Virtual Machines exists in same region and same resource group and 
   storage of Cloudcenter environment
	
## How it works
   1. Import the service and application profile using Import service script. Refer 
   section ## Importing the service.It creates application profiles Azure_Restore.
   
   2. There are number of ways to restore a VM.
         1. AlternateLocation - creates and gets a basic VM up and running from a restore point 
		 2. RestoreDisks - Restores a VM disk, which can then be used to create a new VM
		 3. OriginalLocation - You can restore a disk, and use it to replace a disk on the existing VM.The current VM must 
			exist. If it's been deleted, this option can't be used.
   
   3. After your successful deployment, the restoration of Azure VirtualMachine from Recovery Service vault will be done based 
   on the any one of above options we selected.To view operations for the restore job, click Backup jobs in vault, and then click the relevant VM
   in azureportal(https://portal.azure.com/)
   
    
   ## Docker Install

1. Install Docker by following the steps provided [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/dockerimages/Steps%20for%20Installation%20of%20Docker%20CE%20on%20CentOS7_V2.docx), on any linux based client machine.

**NOTE** : You can skip the above step, if Docker Client is already installed and running in your machine. 
- You can check , if docker is installed , by running "docker -v"
- You can check , if docker is running , by executing the command "systemctl status docker"
 	

## Pre-Requisites
#### CloudCenter
- CloudCenter 5.x.x and above.
- Knowledge on how to use Workload Manager. 
 

## Importing the service

Step 1 : Download the service import utility file  from [here](https://raw.githubusercontent.com/datacenter/cloudcentersuite/master/Content/Scripts/ServiceImportMaster.sh), and save the file on to your linux machine.
- wget command may not be installed. Need to execute "yum install wget -y" in case of centos7.

	    Example: 
      wget https://github.com/datacenter/cloudcentersuite/raw/master/Content/Scripts/ServiceImportMaster.sh
				
- After downloading ServiceImportMaster.sh, provide file permissions by executing "chmod 755 ServiceImportMaster.sh".

Step 2 : Execute the script from Step 1 using the following command.

        sh ServiceImportMaster.sh

Once the script is run, please follow the prompts to import the service or the corresponding application profile.

##### PLEASE NOTE : You be prompted with location of service bundle zip on client machine. The files must be copied on to the repository before proceeding to deploy.

         - Service Zip file under <service_path>/<your_bundle_name>
                    
             Example : http://<Your_REPO_Server_IP>/<service_path>/azurerestore.zip
			 

## Service Package Bundle

The Packer Service bundle consists of the following files:

Shell script:
 - service: Initiates the python script to start integration.

Python script :
 - azure_restore.py : script that invokes the rest APIs to restore AzureVMs. 
 - main.py - calling functions based on operations like start
 - util.py: utility file
 - error_messages.json : Json file contains error messages.
 - error_utils.py: The script that handles error functionality.
  

## External Lifecycle Actions
    - External Action Bundle:   http://YourIP/services/azurerestore.zip
    - External Lifecycle Actions:
        Start:
            Script from bundle: service start


## Deployment Parameters:
| Parameter Name| Type	 | Mandatory |Description |  
| ------ | ------ | ------ | ------   
| vaultname |	String | Yes | Name of the Recovery vault where backups exists. |
| vm_name | String | Yes | Azure Virtual Machine name which we need to recover from backup. | 
| policyname | String | Yes | Backup policy name for vaultname provided.  |
| recoverypointdate | String | Yes | Recoverypoint Date from list of backups.  |
| restore_type | String | Yes | Type of Restoration.  |
| newvm | String | Yes | New virtualmachine name if we restore in new Virtual Machine.  |






import requests
import json
import time
import os
import sys
import datetime
from util import *

def  get_accesstoken(tenantid, client_id, client_secret):
    '''GET access token for Authorization'''
    endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(tenantid)
    resource ="https://management.azure.com/"
    grant_type = "client_credentials"
    payload = {"client_id": client_id, "client_secret":client_secret,
               "resource":resource, "grant_type":grant_type}
    response = requests.post(url= endpoint, data=payload)
    json_resp = response.json()
    if response.status_code == 200:
        return json_resp["access_token"]
    else:
        print_log("No Access token")
        sys.exit(127)

def restore_position(subscription_id, resource_group, vaultname, policyid, tenantid, vmname,
                     client_id, client_secret, protectedItemName, containerName, virtualmachineid,
                     sourceresourceid, recoverypoindate, recoverypointid, location, vnet, restoretype, storage, newvm):
    '''RESTORE VM'''
    access_token = get_accesstoken(tenantid, client_id, client_secret)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + access_token}
    endpoint = "https://management.azure.com/Subscriptions/{}/resourceGroups/{}/" \
               "providers/Microsoft.RecoveryServices/vaults/{}/backupFabrics/Azure/" \
               "protectionContainers/{}/protectedItems/{}/recoveryPoints/{}/restore?" \
               "api-version=2016-12-01".format(subscription_id, resource_group, vaultname, containerName, protectedItemName, recoverypointid)
    if restoretype == "AlternateLocation" and len(newvm) > 0:
        vmname = newvm
    if restoretype  == "RestoreDisks":
        payload = {
              "properties": {
                "objectType": "IaasVMRestoreRequest",
                "recoveryPointId": recoverypointid,
                "recoveryType": restoretype,
                "sourceResourceId": sourceresourceid,
                "storageAccountId": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Storage/storageAccounts/{}".format(subscription_id, resource_group, storage),
                "region": location,
                "createNewCloudService": False,
                "originalStorageAccountOption": False,
                "encryptionDetails": {
                  "encryptionEnabled": False
                }
              }
            }
    else:
        payload = {
            "properties": {
              "objectType":  "IaasVMRestoreRequest",
              "recoveryPointId": recoverypointid,
              "recoveryType": restoretype,
              "sourceResourceId": sourceresourceid,
              "storageAccountId": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Storage/storageAccounts/{}".format(subscription_id, resource_group, storage),
              "targetVirtualMachineId": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Compute/virtualMachines/{}".format(subscription_id, resource_group, vmname),
              "targetResourceGroupId": "/subscriptions/{}/resourceGroups/{}".format(subscription_id, resource_group),
              "virtualNetworkId": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/virtualNetworks/{}".format(subscription_id, resource_group, vnet),
              "subnetId": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/virtualNetworks/{}/subnets/default".format(subscription_id, resource_group, vnet),
              "region": location,
              "createNewCloudService": False,
              "originalStorageAccountOption": False,
              "encryptionDetails": {
                "encryptionEnabled": False
              }
            }


        }
    restore_endpoint = requests.post(url=endpoint, headers=headers, data = json.dumps(payload))
    if restore_endpoint.status_code == 200 or restore_endpoint.status_code == 202:
        vm_restore_endpoint = restore_endpoint.headers['Azure-AsyncOperation']
        vm_restore = requests.get(url=vm_restore_endpoint, headers=headers)
        print_log(vm_restore.status_code)
        if vm_restore.status_code == 200 or vm_restore.status_code == 202:
            print_log("Restore VM Success")


def get_recovery_point(subscription_id, resource_group, vaultname, policyid, tenantid,
                       vmname, client_id, client_secret, protectedItemName, containerName,
                       virtualmachineid, sourceresourceid, restoretype, recoverypoindate,
                       location, vnet, storage, newvm):
    '''GET RECOVERY POINT'''
    endpoint = "https://management.azure.com/Subscriptions/{}/resourceGroups/{}/" \
               "providers/Microsoft.RecoveryServices/vaults/{}/backupFabrics/" \
               "Azure/protectionContainers/{}/protectedItems/{}/recoveryPoints" \
               "?api-version=2016-12-01".format(subscription_id, resource_group, vaultname,
                                                containerName, protectedItemName)
    access_token = get_accesstoken(tenantid, client_id, client_secret)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + access_token}
    res = requests.get(url=endpoint, headers=headers)
    listrecoverypoint = res.json()
    if res.status_code == 200 or res.status_code == 201:
        for i in listrecoverypoint['value']:
            recoverypointtime = i["properties"]["recoveryPointTime"]
            print_log(recoverypointtime)
            if recoverypointtime.startswith(recoverypoindate) :
                recoverypointid = i["name"]
                restore_position(subscription_id, resource_group, vaultname, policyid,
                                 tenantid, vmname, client_id, client_secret, protectedItemName,
                                 containerName, virtualmachineid, sourceresourceid, recoverypoindate,
                                 recoverypointid, location, vnet, restoretype, storage, newvm)
    else:
        print_log("Error in recovery point api")
        sys.exit(127)

def restore_vm(subscription_id, resource_group, vaultname, tenantid,
               location, policyname, vmname, client_id, client_secret, restoretype,
               recoverypoindate, vnet, storage, newvm):
    '''List Backup for Recovery valut'''
    backup_lists = "https://management.azure.com/Subscriptions/{}/resourceGroups/{}" \
                   "/providers/Microsoft.RecoveryServices/vaults/{}/backupProtectedItems?" \
                   "api-version=2017-07-01&$filter=backupManagementType eq 'AzureIaasVM' and " \
                   "itemType eq 'VM'".format(subscription_id, resource_group, vaultname)
    access_token = get_accesstoken(tenantid, client_id, client_secret)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + access_token}
    response = requests.get(url=backup_lists, headers=headers)
    listvault = response.json()
    if response.status_code == 200 or response.status_code == 201:
        for i in listvault['value']:
            print_log(i["properties"]["friendlyName"])
            if i["properties"]["friendlyName"] == vmname:
	        print_log("VM matches")
                protectedItemName = i["name"]
                containerName = "IaasVMContainer;" + i["properties"]["containerName"]
                virtualmachineid = i["properties"]["virtualMachineId"]
                sourceresourceid = i["properties"]["sourceResourceId"]
                policyid = i["properties"]["policyId"]
                get_recovery_point(subscription_id, resource_group, vaultname, policyid, tenantid, vmname,
                                   client_id, client_secret, protectedItemName, containerName,
                                   virtualmachineid, sourceresourceid, restoretype, recoverypoindate,
                                   location, vnet, storage, newvm)
            else:
		sys.exit(127)
                print_log("vm not exists")
    else:
        print_log("No backuplist for vault")
        sys.exit(127)

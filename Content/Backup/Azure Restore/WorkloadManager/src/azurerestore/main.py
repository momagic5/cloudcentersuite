import sys
import os
from azure_restore import *
from util import *
from error_utils import ErrorUtils

APP_ID = os.environ["CliqrCloud_ClientId"]
TENANT_ID = os.environ["CliqrCloud_TenantId"]
PASSWORD = os.environ["CliqrCloud_ClientKey"]
SUBSCRIPTION = os.environ["CliqrCloudAccountId"]
RESOURCE = os.environ["Cloud_Setting_ResourceGroup"]
LOCATION = os.environ["region"]
VAULTNAME = os.environ["vaultname"]
POLICYNAME = os.environ.get("policyname","DefaultPolicy")
VMNAME = os.environ["vm_name"]
print_log(os.environ.has_key("restore_type"))
RESTORE_TYPE = os.environ["restore_type"]
RECOVERYPOINTDATE = os.environ["recoverypointdate"]
VNETW = os.environ["Cloud_Setting_VirtualNetwork"].split(' ')
VNET = VNETW[1]
Cloud_Setting_StorageAccount = os.environ["Cloud_Setting_StorageAccount"].split(' ')
STORAGE = Cloud_Setting_StorageAccount[1]
NEW_VM = os.environ["newvm"]

arg1 = sys.argv[1]
print_log(arg1)
try:
    if arg1 == 'restorevm':
        restore_vm(SUBSCRIPTION, RESOURCE, VAULTNAME, TENANT_ID, LOCATION,POLICYNAME, VMNAME, APP_ID, PASSWORD,
                   RESTORE_TYPE, RECOVERYPOINTDATE, VNET, STORAGE, NEW_VM)
except Exception as e:
    write_error(e)
    print_error(e)

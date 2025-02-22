import sys
import os
from azure_backup import *
from util import *
from error_utils import ErrorUtils

APP_ID = os.environ["CliqrCloud_ClientId"]
TENANT_ID = os.environ["CliqrCloud_TenantId"]
PASSWORD = os.environ["CliqrCloud_ClientKey"]
SUBSCRIPTION = os.environ["CliqrCloudAccountId"]
RESOURCE = os.environ["Cloud_Setting_ResourceGroup"]
LOCATION = os.environ["region"]
VAULTNAME = os.environ["vaultname"]
POLICYNAME = os.environ.get("policyname")
if(len(POLICYNAME) > 0):
    POLICYNAME = os.environ.get("policyname")
else:
    POLICYNAME = "DefaultPolicy"
print_log(POLICYNAME)
DEPENDENTS = os.environ.get('CliqrDependencies', '')
print_log(len(DEPENDENTS))
if(len(DEPENDENTS) > 0):
    VMNAME = os.environ.get('CliqrTier_'+DEPENDENTS+'_HOSTNAME')
else:
    VMNAME = os.environ["vm_name"]
print_log(VMNAME)

arg1 = sys.argv[1]
try:
    if arg1 == 'backupvm':
        create_recovery_vault(SUBSCRIPTION, RESOURCE, VAULTNAME, TENANT_ID, LOCATION,POLICYNAME, VMNAME, APP_ID, PASSWORD)
    elif arg1 == 'stopbackup':
        deletebackup(SUBSCRIPTION, RESOURCE, VAULTNAME, TENANT_ID, LOCATION,POLICYNAME, VMNAME, APP_ID, PASSWORD)
except Exception as e:
    print_log(e)
    write_error(e)
    print_error(e)

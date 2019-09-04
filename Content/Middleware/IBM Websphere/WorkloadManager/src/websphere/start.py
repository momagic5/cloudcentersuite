import os
from util import *

if is_primary_node():
    print "Deploying Application and Starting Cluster, Servers and Application..."
    execfile('./wsadminlib.py')

    cluster_name = "mycluster"
    application_name = os.environ.get("applicationName", "demo application")

    args = ['-cluster ' + cluster_name,'-appname', application_name,'-target', 'default','-usedefaultbindings','-defaultbinding.virtual.host', 'default_host']
    app_path = os.environ.get('appPackage', False)
    if app_path:
        AdminApp.install(app_path.strip(), args)

    saveAndSync()
    # Start Cluster, Servers and Application
    startCluster(cluster_name)
    startAllServersInCluster(cluster_name)
    startApplication(application_name)

    saveAndSync()
    # Save and Sync with All Nodes
    
else:
    print "Secondary Nodes- no action"


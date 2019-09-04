import os
from util import *

if is_primary_node():
    print "Stopping All servers in cluster..."
    print "Stopping Application..."
    
    execfile('./wsadminlib.py')

    cluster_name = "mycluster"
    application_name = os.environ.get("applicationName", "demo application")

    # Stop Deployed Application and Servers in Cluster
    stopApplication(application_name)
    stopAllServersInCluster(cluster_name)

    # Save and Sync with all Nodes
    saveAndSync()
else:
    print "Secondary Node - No action"

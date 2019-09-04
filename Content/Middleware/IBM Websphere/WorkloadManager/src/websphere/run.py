import os

execfile('./wsadminlib.py')

cell = AdminControl.getCell()
cluster_name = "mycluster"
cluster = createCluster(cell,cluster_name)
if cluster:
    node_ids = listNodes()

    for nid in node_ids:
        server_name = "server-" + nid
        createServerInCluster(cluster_name,nid,server_name)

saveAndSync()

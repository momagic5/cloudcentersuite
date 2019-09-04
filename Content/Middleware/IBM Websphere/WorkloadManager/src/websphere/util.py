import os

# Get All Nodes
def get_all_nodes():
    nodes = []
    try:
        app_tier_name = os.environ.get("cliqrAppTierName", False)
        if not app_tier_name:
            sys.exit(127)

        nodes = str(os.environ['CliqrTier_' + app_tier_name + '_HOSTNAME']).split(',')
    except Exception, err:
        print err
        sys.exit(127)

    return nodes

def is_primary_node():
    num_of_nodes = os.environ.get("NumNodes", 1)
    if int(num_of_nodes) == 1:
        return True

    nodes=get_all_nodes()
    node=os.environ.get('cliqrNodeHostname', False)
    if not node:
        return False
    
    if nodes[0] in node:
        return True

    return False

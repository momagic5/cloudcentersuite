#!/usr/bin/env python

import os
from subprocess import STDOUT, check_call
import pip
import sys
from util import *
from error_utils import ErrorUtils


'''
    Required Azure Python Packages
'''
pip_sources = [
    "boto3"
]

cmd = sys.argv[1]

# Install Python Packages
try:
    from pip import main 
except ImportError as err:
    from pip._internal import main

def install_packages():
    global pip_sources
    main(['install'] + pip_sources)

# Validate Mandatory parameters
# Invoke External LifeCyle Actions

try:
    print('check prequistes environments')
    #from service_parameter_util import create_params_json
    #status = create_params_json()
    status = 1

    if bool(status):
        print("Prequistes success.............")
        
        print_log("Initializing")
        install_packages()

        from main import main
        main(cmd)
    else:
        #print_error(ErrorUtils.internal_error())
        sys.exit(127)

except Exception as e:
    print_error(ErrorUtils.internal_error(e.message))
    write_error(e)

    sys.exit(127)

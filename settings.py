#
# Author: jun10000 (https://github.com/jun10000)
#

import yaml

# Common Settings
with open('/var/project/onkyori_common/settings.yaml', 'r') as file:
    common = yaml.load(file)

# Waiting time of loop function [s]
WAIT_TIME = 0.001

# Number of input physical pin
INPUT_PIN = 21

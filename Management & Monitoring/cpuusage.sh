

#!/bin/bash

mpstat | grep all | awk -F' ' '{ print $12}' > cpuUsage.txt


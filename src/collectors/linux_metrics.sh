#!/bin/bash
# linux_metrics.sh - Grabs CPU, RAM, and Disk stats

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
DISK_USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')

echo "cpu:$CPU_USAGE,mem:$MEM_USAGE,disk:$DISK_USAGE"

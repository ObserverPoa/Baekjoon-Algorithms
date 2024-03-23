# https://www.acmicpc.net/problem/1700

import sys
import collections

N, K = map(int, sys.stdin.readline().split())

device_ids = list(map(int, sys.stdin.readline().split()))

device_queues = collections.defaultdict(list)

for i in range(len(device_ids) - 1, -1, -1):
    device_queues[device_ids[i]].append(i)

using_devices = set()
removed_count = 0

def get_latest_device():
    latest_device = None
    max_index = -1

    for using_device in using_devices:
        queue = device_queues[using_device]

        if not queue:
            return using_device

        if queue[-1] > max_index:
            max_index = queue[-1]
            latest_device = using_device
    
    return latest_device


for device_id in device_ids:
    if len(using_devices) >= N and device_id not in using_devices:
        removed_count += 1
        latest_device = get_latest_device()
        using_devices.remove(latest_device)
        
    using_devices.add(device_id)
    device_queues[device_id].pop()

print(removed_count)
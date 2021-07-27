import psutil


print(psutil.cpu_stats())

print(psutil.disk_usage("C:"))

print(psutil.virtual_memory())

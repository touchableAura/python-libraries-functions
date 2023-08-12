import os 
import psutil 

# like ps utility 
# shows us what is going on with our system


# # kind='inet4' targets ipV4 connections 
# # turns all port numbers, [0] takes fist item in list (just for demo)
# print("NETWORK:\n", psutil.net_connections(kind='inet4')[0], "\n")
# print("USERS: \n", psutil.users(), "\n") # pull all connected users 
# print("PIDs:\n", psutil.pids(), "\n") # all process ids for running programs right now

# process iteration  
# make a cleaner list of what is going on 
for proc in psutil.process_iter(['pid', 'name', 'username']):
   print(proc.info)

"""
# p = psutil.Process() accepts a pid# from above and 
# saying give me all the information on this particular process
p = psutil.Process(pid=1952)
with p.oneshot():
    print("\nName: " + str(p.name()))
    print("CPU Time: " + str(p.cpu_times()))
    print("CPU %: " + str(p.cpu_percent()))
    print("Created Time: " + str(p.create_time()))
    print("PPID: " + str(p.ppid()))
    print("Status: " + str(p.status()))

"""
"""
print("CPU times:", psutil.cpu_times())
print("CPU in use:", psutil.cpu_percent(interval=.1), "%")
print("Memory in use:", psutil.virtual_memory().percent,"%")
print("Disk usage", psutil.disk_usage('/').percent, "%" )
print("Memory free:", psutil.virtual_memory().available/(1024**3), "GB") 
print("Disk usage", psutil.disk_usage('/').free/(1024**3), "GB")
print(psutil.disk_partitions())
print(psutil.users())
print(psutil.boot_time())

"""


# function to pull information about just this process
# useful when going through the list and you want to know more about it 
# where did it come from, who are it's parents 
def find_process_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []

    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls

print(find_process_by_name("winlogon.exe"))







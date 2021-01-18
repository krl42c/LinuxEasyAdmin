import psutil,sys,os,subprocess


# Returns the current platform the program is running in
def get_os():
    return str(sys.platform)
# Returns a list with the current processes that are running
# TODO: change list to dictionary, add PID to be able to make operations with them
def get_process_list():
    processList = []

    for p in psutil.process_iter():
        pName = p.name()
        processList.append(str(pName) + "\n")

    return processList;

def get_process_list_with_usage():
    processList = []

    for p in psutil.process_iter():
        # processList.append({str(p.name()) : str(p.memory_percent())})
        processList.append({"Name" : str(p.name()), "Value" : str(round(p.memory_percent(),3))})

    return processList

# Receives a disk as "/dev/hdx" and returns it currents space, if no argument is passed
# returns the whole disk size
def get_disk_space(disk=None):
    hd_space = None
    if disk is None:
        hd_space = psutil.disk_usage('/')
    else:
        hd_space = psutil.disk_usage(disk)

    return hd_space[3]

# Returns the percentage of the battery
def get_battery_percentage():
    battery = psutil.sensors_battery()
    return str(battery.percent)

def get_ram_usage_percent():
    return psutil.virtual_memory().percent

def get_ram():
    return psutil.virtual_memory()

def get_cpu_usage():
    # TODO: esto no funciona, no se que hacer me quiero suicidar
    return psutil.cpu_percent()

def apt_locked():
    output = subprocess.check_output("ps -C apt-get,dpkg >/dev/null && echo 'LOCK' || echo 'FREE'", shell=True)
    return output.rstrip()

def get_disk_folders():
    size_folder = []

    sizes = subprocess.check_output("du -h -d1 ~ | cut -f1",shell=True)
    folders = subprocess.check_output("du -h -d1 ~ | cut -f2",shell=True)

    sizes_str = str(sizes).split('\\n')
    folders_str = str(folders).split('\\n')

    for i,j in zip(sizes_str,folders_str):
        size_folder.append({"Name" : j , "Value" : i })

    return size_folder


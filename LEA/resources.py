import psutil,sys


#Returns the current platform the program is running in
def getOS():
    return str(sys.platform)

#Returns a list with the current processes that are running
#TODO: change list to dictionary, add PID to be able to make operations with them
def getProcessList():
    processList = []

    for p in psutil.process_iter():
        pName = p.name()
        processList.append(str(pName))

    return processList;

#Receives a disk as "/dev/hdx" and returns it currents space, if no argument is passed
#returns the whole disk size
def getDiskSpace(disk=None):
    hd_space = None
    if disk is None:
        hd_space = psutil.disk_usage('/')
    else:
        hd_space = psutil.disk_usage(disk)

    return hd_space

#Returns the percentage of the battery
def getBatteryPercentage():
    battery = psutil.sensors_battery()
    return str(battery.percent)

def getRAMUsagePercent():
    return psutil.virtual_memory().percent

def getRAM():
    return psutil.virtual_memory()



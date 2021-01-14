import os
def delete_process(process):
    return os.system("killall " + process.rstrip())

def get_process_pid(process):
    pass


def get_process_status(process):
    pass

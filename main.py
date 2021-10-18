from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import psutil
import shutil


app = FastAPI()

def memory():
    return psutil.virtual_memory().total - psutil.virtual_memory().available

@app.get("/metrics", response_class=PlainTextResponse)
async def main():
    disk_usage = shutil.disk_usage("/")
    return_string = ""
    return_string += f"# HELP go_hostsystemmonitor_cpu Current CPU Usage percentage ish\n# TYPE go_hostsystemmonitor_cpu gauge\ngo_hostsystemmonitor_cpu {str(psutil.cpu_percent())}\n"
    return_string += f"# HELP go_hostsystemmonitor_mem Current Mem usage in mb\n# TYPE go_hostsystemmonitor_mem gauge\ngo_hostsystemmonitor_mem {str(memory())}\n"
    return_string += f"# HELP go_disc_total Current disc usage \n# TYPE go_disc_total gauge\ngo_disc_total {str(disk_usage.total)}\n"
    return_string += f"# HELP go_disc_usage Current disc usage \n# TYPE go_disc_usage gauge\ngo_disc_usage {str(disk_usage.used)}\n"
    return return_string

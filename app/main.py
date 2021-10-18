from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import psutil

app = FastAPI()

def memory():
    return psutil.virtual_memory().total - psutil.virtual_memory().available

@app.get("/metrics", response_class=PlainTextResponse)
async def main():
    return f"# HELP go_hostsystemmonitor_cpu Current CPU Usage percentage ish\n# TYPE go_hostsystemmonitor_cpu gauge\ngo_hostsystemmonitor_cpu {str(psutil.cpu_percent())}\n# HELP go_hostsystemmonitor_mem Current Mem usage in mb\n# TYPE go_hostsystemmonitor_mem gauge\ngo_hostsystemmonitor_mem {str(memory())}" 

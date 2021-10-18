const express = require('express')
const app = express()
const port = 3000
const ip = require('ip')
const os = require("os-utils");

function cpu() {
    return new Promise((resolve, reject) => {
        os.cpuUsage((v) => {
            console.log(v)
            resolve(v);
        });
    });
}

function mem() {
    return os.totalmem() - os.freemem() 
}

app.get('/metrics', async (req, res) => {
    res.send(`# HELP go_hostsystemmonitor_cpu Current CPU Usage percentage ish\n# TYPE go_hostsystemmonitor_cpu gauge\ngo_hostsystemmonitor_cpu ${await cpu()}\n# HELP go_hostsystemmonitor_mem Current Mem usage in mb\n# TYPE go_hostsystemmonitor_mem gauge\ngo_hostsystemmonitor_mem ${mem()}`)
});

app.listen(port, () => {
    console.log(`\nApp running at:\n- Local: \x1b[36mhttp://localhost:${ port }/\x1b[0m\n- Network \x1b[36mhttp://${ ip.address() }:${ port }/\x1b[0m\n\nTo run for production, run \x1b[36mnpm run start\x1b[0m`)
});
const net = require('net')
const { exit } = require('process')

const HOST = "127.0.0.1"
const PORT = 1234
const URL = "ws://" + HOST + ":" + PORT + "/"
console.log(URL)

let sock = new net.Socket()
sock.connect(PORT, HOST)

sock.on("connect", () => {
    let obj = {
        'field1': 12345,
        'field2': "Hello world from Javascript!"
    }
    let obj_str = JSON.stringify(obj)
    console.log("sending object: " + obj_str)
    sock.write(obj_str)
    sock.destroy()
    console.log("done")
    exit()
})
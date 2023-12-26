const net = require('net')
const { exit } = require('process')

const HOST = "127.0.0.1"
const PORT = 1234
const URL = "ws://" + HOST + ":" + PORT + "/"
console.log(URL)

let sock = new net.Server()
sock.listen(PORT, HOST)

sock.on("connection", (con) => {
    con.on("data", (data) => {
        obj = JSON.parse(data)
        console.log("received object:")
        console.log(obj)
        con.destroy()
        exit()
    })
})
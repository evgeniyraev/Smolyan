// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

const { SerialPort } = require('serialport')
const tableify = require('tableify')

async function listSerialPorts() {
  await SerialPort.list().then((ports, err) => {
    if(err) {
      document.getElementById('error').textContent = err.message
      return
    } else {
      document.getElementById('error').textContent = ''
    }
    console.log('ports', ports);

    if (ports.length === 0) {
      document.getElementById('error').textContent = 'No ports discovered'
    }

    tableHTML = tableify(ports)
    document.getElementById('ports').innerHTML = tableHTML
  })
}

let sights = [
  "aquarius",
  "aries",
  "cancer",
  "capricorn",
  "gemini",
  "leo",
  "libra",
  "pisces",
  "sagittarius",
  "scorpio",
  "taurus",
  "virgo",
]

let questionView = document.getElementById("question")
let resultLabel = document.getElementById("result_label")
let resultIcon = document.getElementById("result_icon")

let randomElement = "aquarius"//sights[Math.random()*sights.length >> 0]


questionView.setAttribute("sign", randomElement)
questionView.setAttribute("stage", 2)

/*
const path = app.getPath("userData")
// write file
const userData = JSON.stringify({serialNumber: 000, email: "a@g.com"})
fs.writeFile(`${path}/user-data.json`, userData)

// read file
fs.readFile(path, {encoding: 'utf-8'}, (err,data)=> {
if (err)return null
updateGlobalStore(JSON.parse(data))
})
*/

const port = new SerialPort({
  path: '/dev/tty.usbserial-2110',
  baudRate: 115200,
})

port.on('data', function (data) {
  console.log('Data:', data.toString())
})

// Open errors will be emitted as an error event
port.on('error', function(err) {
  console.log('Error: ', err.message)
})

//setTimeout(listPorts, 2000);

//listSerialPorts()

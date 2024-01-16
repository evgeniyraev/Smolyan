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
  "aries",
  "taurus",
  "gemini",
  "cancer",
  "leo",
  "virgo",
  "libra",
  "scorpius",
  "sagittarius",
  "capricornus",
  "aquarius",
  "pisces",
]

let questionView = document.getElementById("question")
let result = document.getElementById("result")

let selectedElement = -1
let stage = 1

function selectElement() {
  let next;
  do {
    next = sights[Math.random() * sights.length >> 0]
  } while(next == selectElement)
  console.log

  selectedElement = next

  updateQuestion()
  updateResult(null)
}

selectElement()

function updateResult(r) {
    result.setAttribute("answer", r)

    if(r == "correct") {
      stage = 4
    } else if (r == null) {
      stage = 1
    } else {
      stage = Math.min(stage + 1, 4)
    }

    questionView.setAttribute("stage", stage)
    
    if(stage == 4) {
      setTimeout(() => {
        selectElement()
      }, 5000)
    }
}

function updateQuestion() {
  questionView.setAttribute("sign", selectedElement)
  questionView.setAttribute("stage", stage)
}

function checkElement(index) {
  if(stage == 4) {
    return
  }

  let choice = sights[index]

  console.log(choice, selectedElement)

  if(choice == selectedElement) {
    updateResult("correct")
  } else {
    updateResult("incorrect")
  }
}
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
  let r = data.toString()

  console.log(`data: ${r}`)
  checkElement(r)
})

// Open errors will be emitted as an error event
port.on('error', function(err) {
  console.log('Error: ', err.message)
})

document.addEventListener("keydown", (e) => {
  if (!e.repeat) {
    let k = e.key
    if(/\d/.test(k)) {
      console.log("---")
      checkElement(k)
    }
    console.log(`Key "${e.key}" pressed [event: keydown]`);
  } else {
    console.log(`Key "${k}" repeating [event: keydown]`);
  }
});


listSerialPorts()

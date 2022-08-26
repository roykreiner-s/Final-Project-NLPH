const express = require("express");
const app = express();
const cors = require("cors");

const PYTHON_PATH = "/Users/noamkesten/PycharmProjects/Final-Project-NLPH/Parser/parser.py";

app.use(cors({ origin: "*" }));

app.get("/text", async (req, res) => {
  console.log("hey", req.query);
  // todo call python method

  const { spawn } = require("child_process");
  const pythonProcess = spawn("python", ["main.py", req.query.text]);
  let x = await setTimeout(() => {}, 1);
  pythonProcess.stdout.on("data", function (data) {
    console.log(data.toString());
    // timeout of 3 seconds
    res.send(data);
    // res.end("end");
  });

  //   const PythonShell = require("python-shell").PythonShell;

  //   var options = {
  //     mode: "text",
  //     // pythonPath: "path/to/python",
  //     pythonOptions: ["-u"],
  //     scriptPath: "/Users/noamkesten/PycharmProjects/Final-Project-NLPH/Parser",
  //     args: ["value1", "value2", "value3"],
  //   };

  //   PythonShell.run("parser.py", options, function (err, results) {
  //     if (err) throw err;
  //     // Results is an array consisting of messages collected during execution
  //     console.log("results: %j", results);
  //   });
  //   pythonProcess.stdout.on("data", (data) => {
  //     res.send("output\n" + data);
  //   });
});

app.get("", (req, res) => {
  res.send("Hello world");
});

// running server locally
const port = 3000;
app.listen(port, async () => {
  try {
    console.log("Server running on port", port);
  } catch (error) {
    console.log("error:", error);
  }
});

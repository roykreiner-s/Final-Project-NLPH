const express = require("express");
const app = express();
const utf8 = require("utf8");
const axios = require("axios");
const cors = require("cors");

app.use(cors({ origin: "*" }));

app.get("/text", async (req, res) => {
  try {
    console.log("Handling GET Request /text route", req.query);
    // call YAP api
    let payload = { text: req.query.text };
    let headers = { "Content-type": "application/json; charset=utf-8" };

    let x = JSON.stringify(payload);
    console.log("payload xxx", JSON.parse(x));

    // python http request
    let python_response = await axios.post("http://127.0.0.1:3002", x, headers);
    res.send(python_response.data);
  } catch (err) {
    res.status(500).send("error: " + err.message);
  }
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

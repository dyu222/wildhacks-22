const express = require("express");
const cors = require('cors');
const app = express();

app.use(cors())

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get('/callAPI', (req, res, next) => {
  res.send("api call success");
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, console.log(`Server started on port ${PORT}`));
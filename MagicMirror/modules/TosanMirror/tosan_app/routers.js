const express = require("express");

const mainRouter = new express.Router();

mainRouter.use(express.json());

mainRouter.use("/users", require("./routers/user"));

module.exports = mainRouter;
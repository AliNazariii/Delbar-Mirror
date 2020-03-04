const Sequelize = require("sequelize");
const sqlite3 = require('sqlite3');

const dbDataPath = require("../utils/consts").tosanPath + "/tosan_app/db/dbData";

const sequelize = new Sequelize("tosanApp", null, null, {
	dialectModule: sqlite3,
	dialect: "sqlite",
	storage: dbDataPath
});
sequelize
	.authenticate()
	.then(() => {
		console.log("Connection has been established successfully.");
	})
	.catch(err => {
		console.error("Unable to connect to the database:", err);
	});
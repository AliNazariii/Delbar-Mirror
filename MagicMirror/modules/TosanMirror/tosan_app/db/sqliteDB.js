const Sequelize = require("sequelize");
const sqlite3 = require("sqlite3");

const { dbDataPath } = require("../utils/consts");

const UserModel = require("./models/UserModel");

const sequelize = new Sequelize("tosanApp", null, null, {
	dialectModule: sqlite3,
	dialect: "sqlite",
	storage: dbDataPath,
	pool: {
		max: 10,
		min: 0,
		acquire: 30000,
		idle: 10000
	}
});

const User = UserModel(sequelize, Sequelize);
sequelize.sync();
module.exports = {
	User
};


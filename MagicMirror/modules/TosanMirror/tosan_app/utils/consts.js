const path = require("path");
const tosanPath = path.resolve("./modules/TosanMirror/");
const dbDataPath = path.join(tosanPath, "/tosan_app/db/dbData");

module.exports = {
	tosanPath,
	dbDataPath
};
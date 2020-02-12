const fs = require("fs");

class TosanModule {
	constructor(name) {
		this.name = name;
		this.config = (JSON.parse(fs.readFileSync("./modules/TosanMirror/tosan_modules/config.json").toString()))[name];
		if (!this.config) {
			this.config = {};
		}
	}

	async getDOM() {
		return "Sorry this module does not provide visual DOM";
	}

	getCredits() {
		return "No one is here yet";
	}
}

module.exports = TosanModule;
const path = require("path");

const NodeHelper = require("node_helper");
const jMoment = require("moment-jalaali");
const express = require("express");

jMoment.loadPersian({ usePersianDigits: true, dialect: "persian-modern" });

const defaultFaceDOM = "<img src=\"modules/TosanMirror/tosan_modules/face.gif\" style=\"border:1px solid black;max-width:100%;\">";

const helper = NodeHelper.create({
	// Subclass start method.
	start: function () {
		const self = this;

		this.fetchers = [];
		console.log("\n\n\n\nHello\n\n\n\n\n");

		console.log(path.resolve("./modules/TosanMirror/tosan_modules/face.gif"));

		const router = new express.Router();
		router.use(express.json());

		console.log("Starting node helper for: " + this.name);

		// router.get("/statement", function (req, res) {
		// 	text = req.query.text;
		// 	self.sendSocketNotification("STATEMENT", { "text": text, date: jMoment().format("dddd, LL") });
		// 	res.sendStatus(200);
		// });

		// router.post("/image", function (req, res) {
		// 	var data = "";
		// 	req.on("data", function (chunk) { data += chunk; });
		// 	req.on("end", function () {
		// 		req.rawBody = data;
		// 		req.jsonBody = JSON.parse(data);
		// 		url = req.jsonBody.url;
		// 		console.log(url);
		// 		self.sendSocketNotification("IMAGE", { "imageurl": url });
		// 		res.sendStatus(200);
		// 	});
		// });

		router.get("/face", function (req, res) {
			self.sendSocketNotification("FACE", defaultFaceDOM);
			res.sendStatus(200);
		});

		router.get("/news", async function (req, res) {
			const newsApp = require("../tosan_modules/tosan_news/app");
			self.sendSocketNotification("NEWS", await newsApp.getDOM());
			res.sendStatus(200);
		});

		this.expressApp.use("/tosan_center", router);
	},

	// Subclass socketNotificationReceived received.
	socketNotificationReceived: function (notification, payload) {
		if (notification === "INITIALIZE") {
			this.sendSocketNotification("FACE", defaultFaceDOM);
		}
		console.log("helper received: " + notification);
	}
});

module.exports = helper;
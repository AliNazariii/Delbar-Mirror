const NodeHelper = require("node_helper");
const jMoment = require("moment-jalaali");
const express = require("express");

jMoment.loadPersian({ usePersianDigits: true, dialect: "persian-modern" });

const defaultFaceDOM = "<img src=\"modules/TosanMirror/tosan_modules/face.gif\" style=\"border:1px solid black;max-width:100%;\">";

const helper = NodeHelper.create({
	// Subclass start method.
	start: function () {
		const that = this;

		this.fetchers = [];

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

		function sendError(err, res) {
			console.log(err.message);
			that.sendSocketNotification("ERROR", "");
			res.sendStatus(400);
		}

		router.get("/face", function (req, res) {
			that.sendSocketNotification("FACE", defaultFaceDOM);
			setTimeout(() => {
				that.sendSocketNotification("HIDE", undefined);
			}, 4000);
			res.sendStatus(200);
		});

		router.get("/news", async function (req, res) {
			try {
				const newsApp = require("../tosan_modules/tosan_news/app");
				that.sendSocketNotification("NEWS", await newsApp.getDOM(req.query.topic));
				res.sendStatus(200);
			} catch (err) {
				sendError(err, res);
			}
		});

		router.get("/jokes", async function (req, res) {
			try {
				const jokesApp = require("../tosan_modules/tosan_jokes/app");
				that.sendSocketNotification("JOKES", await jokesApp.getDOM());
				res.sendStatus(200);
			} catch (err) {
				sendError(err, res);
			}
		});

		this.expressApp.use("/tosan_center", router);
	},

	// Subclass socketNotificationReceived received.
	socketNotificationReceived: function (notification, payload) {
		if (notification === "INITIALIZE") {
			require("../tosan_app/main");
			this.sendSocketNotification("FACE", defaultFaceDOM);
		}
		console.log("helper received: " + notification);
	}
});

module.exports = helper;
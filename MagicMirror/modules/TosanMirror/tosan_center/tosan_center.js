//aiclient.js

Module.register("tosan_center", {

	// Default module config.
	defaults: {
		animationSpeed: 0.5 * 1000,
		iconTable: {
			"clear-day": "wi-day-sunny",
			"partly-cloudy-day": "wi-day-cloudy",
			"cloudy": "wi-cloudy",
			"wind": "wi-cloudy-windy",
			"rain": "wi-rain",
			"thunderstorm": "wi-thunderstorm",
			"snow": "wi-snow",
			"fog": "wi-fog",
			"clear-night": "wi-night-clear",
			"partly-cloudy-night": "wi-night-cloudy",
			"hail": "wi-rain",
			"tornado": "wi-rain"
		}
	},

	// Define required translations.
	getTranslations: function () {
		// The translations for the defaut modules are defined in the core translation files.
		// Therefor we can just return false. Otherwise we should have returned a dictionairy.
		// If you're trying to build your own module including translations, check out the documentation.
		return false;
	},

	// Define required scripts.
	getStyles: function () {
		return ["weather-icons.css", "currentweather.css"];
	},

	// Define start sequence.
	start: function () {
		this.currentDOM = "";
		Log.log("Starting module: " + this.name);
		this.sendSocketNotification("INITIALIZE", {});
	},

	// Override dom generator.
	getDom: function () {
		wrapper = document.createElement("div");
		wrapper.innerHTML = this.currentDOM;
		return wrapper;
	},

	// Override socket notification handler.
	socketNotificationReceived: function (domModule, dom) {
		Log.log("received new notifictaion from submodule: " + domModule);
		this.currentDOM = dom;
		this.updateDom(this.config.animationSpeed);
	}
});

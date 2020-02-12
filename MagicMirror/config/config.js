/* Magic Mirror Config Sample
/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 */

var config = {
	port: 8080,

	language: "fa",
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "TosanMirror/tosan_center",
			position: "middle_center" // This can be any of the regions.
		},
		{
			module: "aiclientdebugger",
			position: "bottom_right"
		},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Tehran",
				locationID: "112931",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "178f407a9c21114f67c8f08550d941aa"
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "Tehran",
				locationID: "112931",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "178f407a9c21114f67c8f08550d941aa"
			}
		},
	],

	electronOptions: {
		fullscreen: false,
		width: 800,
		height: 600
	}

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }

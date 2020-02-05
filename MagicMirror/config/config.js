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
			module: "aiclient",
			position: "middle_center" // This can be any of the regions.
		},
		{
			module: "aiclientdebugger",
			position: "bottom_right"
		},
		{
			module: "clock",
			position: "top_left"
		}
	],

	electronOptions: {
		fullscreen: false,
		width: 800,
		height: 600
	}

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }

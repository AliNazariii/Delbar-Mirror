const axios = require("axios");

const TosanModule = require("../TosanModule");
const myModule = new TosanModule("tosan_jokes");

async function getJoke() {
	try {
		const response = await axios({
			"method": "GET",
			"url": "https://joke3.p.rapidapi.com/v1/joke",
			"headers": {
				"content-type": "application/octet-stream",
				"x-rapidapi-host": "joke3.p.rapidapi.com",
				"x-rapidapi-key": "06f1bc444amshca89d03074926ebp17f489jsn549fbdbb579e",
				"nsfw": "false"
			}
		});
		const joke = response.data.content;
		// console.log(joke);
		return joke;
	} catch (err) {
		console.log(err.message);
		return "Sorry, I cannot get joke right now :(";
	}
}

myModule.getDOM = async function () {
	const joke = await getJoke();
	const wrapper = `<div><p>${joke}</p></div>`;
	return wrapper;
};

module.exports = myModule;
const fs = require("fs");

const axios = require("axios");
const xmljs = require("xml-js");

const config = (JSON.parse(fs.readFileSync("./modules/TosanMirror/tosan_modules/config.json").toString())).tosan_news;

async function getData(group) {
	try {
		const newsData = (await axios.get(config[group])).data;
		const jsData = xmljs.xml2js(newsData, { compact: true });

		let list = [];
		for (const dataElement of (jsData.rss.channel.item)) {
			// console.log((jsData.rss.channel.item));
			list = list.concat(dataElement.title._text);
		}
		return list;
	} catch (err) {
		return ["Cannot get news sorry :("];
	}
}

async function getDOM(group = "all") {
	const dataList = await getData(group);
	let inner = "";
	for (let i = 0; i < Math.min(5, dataList.length); i++) {
		inner += `<p>${dataList[i]}</p>\n<br>`;
	}
	const wrapper = `<div style="font-size:20px;line-height:10px">${inner}</div>`;
	return wrapper;
}

module.exports = {
	getDOM
};
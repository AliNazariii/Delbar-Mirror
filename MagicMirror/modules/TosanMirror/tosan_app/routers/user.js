const router = new (require("express")).Router();
const { User } = require("../db/sqliteDB");

async function findByParamId(req, res, next) {
	try {
		const user = await User.findOne({ where: { id: req.params.id } });
		if (!user) {
			return res.send(404).send();
		}
		req.user = user;
		next();
	} catch (err) {
		return res.status(500).send(err.message);
	}
}

router.post("/", async (req, res) => {
	try {
		User.create(req.body);
		await User.sync();
		res.status(201).send();
	} catch (err) {
		res.status(500).send(err.message);
	}
});

router.get("/", async (req, res) => {
	const users = await User.findAll();
	res.send(users);
});

router.get("/:id", findByParamId, async (req, res) => {
	res.send(req.user);
});

router.patch("/:id", findByParamId, async (req, res) => {
	try {
		const validUpdates = ["name"];
		const updates = (Object.keys(req.body)).filter((update) => validUpdates.includes(update));
		const newUser = {};
		for (update of updates) {
			newUser[update] = req.body[update];
		}
		const updatedUser = await req.user.update(newUser);
		res.send(updatedUser);
	} catch (err) {
		res.status(500).send(err.message);
	}
});

router.delete("/:id", findByParamId, async (req, res) => {
	try {
		await req.user.destroy();
		res.send();
	} catch (err) {
		res.status(500).send(err.message);
	}
});

module.exports = router;
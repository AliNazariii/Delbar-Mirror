function defineModel(sequelize, type) {
	const model = {
		id: {
			type: type.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		name: type.STRING
	};
	return sequelize.define("User", model);
}

module.exports = defineModel;
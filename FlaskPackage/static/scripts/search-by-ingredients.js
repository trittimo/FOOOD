function addIngredients() {
	var form = document.getElementById("ingredient-form");
	for (i = 0; i < 5; i++) {
		var element = document.createElement("input");
		element.type = "text";
		form.appendChild(document.createTextNode("INGREDIENT: "));
		form.appendChild(element);
		form.appendChild(document.createElement("br"));
	}
}

function submitIngredients() {
	var inputs = document.getElementById("ingredient-form").getElementsByTagName("input");
	var ingredients = [];

	for (i = 0; i < inputs.length; i++) {
		ingredients[i] = inputs.value
	}

	
}
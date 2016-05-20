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
	var form = document.getElementById("ingredient-form");
	var inputs = form.getElementsByTagName("input");
	var ingredients = [];

	for (i = 0; i < inputs.length; i++) {
		if (inputs[i].value) {
			ingredients.push(inputs[i].value)
		}
	}
	
	var field = document.createElement("input")
	field.setAttribute("type", "hidden");
	field.setAttribute("name", "ingredients");
	field.setAttribute("value", JSON.stringify(ingredients));
	form.appendChild(field);
	form.submit();
}
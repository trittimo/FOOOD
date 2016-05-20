function cancelOrder(id, username, session) {
	var form = document.getElementsByTagName("form")[0];
	var eid = document.createElement("input");
	eid.setAttribute("type", "hidden");
	eid.setAttribute("name", "id");
	eid.setAttribute("value", "" + id);
	var esess = document.createElement("input");
	esess.setAttribute("type", "hidden");
	esess.setAttribute("name", "session");
	esess.setAttribute("value", "" + session);
	var euser = document.createElement("input");
	euser.setAttribute("type", "hidden");
	euser.setAttribute("name", "user");
	euser.setAttribute("value", "" + username);
	form.appendChild(eid);
	form.appendChild(esess);
	form.appendChild(euser);
	// document.getElementsByTagName("body")[0].appendChild(form);
	
	form.submit();
}
//javascript functions called within the client gui html pages.
function authenticateThenGoTo(goToLink) {
  //TOD0: check to see if the user is still logged in
  window.location.href = goToLink;
}

function logout() {
  //TODO: sign the user out
  alert("Logged out! Click to proceed.");
  window.location.href = "./login.html";
}


function goBack() {
  window.history.back();
}


//the parameter, type, is either "area", "issue", or "employee"
function deleteElement(elementType) {
  //TODO: pop up to confirm the deletion.
  //communicate to backend to delete the correct entry
  //reload the table with the just-deleted entry gone.
  alert("You're about to delete!");
  window.location.href = "./edit-employee.html";
}

//TODO: implement the same two functions above for Issues and Areas. You can probably generalize all delete functions to single function if you want.

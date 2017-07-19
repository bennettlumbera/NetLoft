var modal = document.getElementById('myModal');
// Get the modal

var btn = document.getElementById('loginClick');
console.log(btn);
// Get the button that opens the modal

var span = document.getElementsByClassName("close")[0];
console.log(span);
// Get the <span> element that closes the modal

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  // When the user clicks on <span> (x), close the modal
  modal.style.display = "none";
}

window.onclick = function(event) {
  // When the user clicks anywhere outside of the modal, close it
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

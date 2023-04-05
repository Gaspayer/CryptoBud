document.getElementById("username-link").addEventListener("click", function(e) {
  e.preventDefault();
  var userDetails = document.querySelector(".user-details");
  userDetails.classList.toggle("d-none");
});

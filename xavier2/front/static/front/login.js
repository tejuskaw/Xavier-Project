const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", function(e){
  container.classList.add("right-panel-active")
  document.querySelector('title').innerHTML = 'Sign up'
} );

signInButton.addEventListener("click", function(e){
  container.classList.remove("right-panel-active")
  document.querySelector('title').innerHTML = 'Sign in'
} );

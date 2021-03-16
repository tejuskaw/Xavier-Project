
let user = document.getElementById('id_username') ;
if (user != null) {
user.placeholder='Username' ; }

let pass = document.getElementById('id_password') ;
if (pass != null) {
pass.placeholder='Password' ;}





let short = document.getElementById('short') ;
let mcq = document.getElementById('mcq') ;

if (short != null) { 

short.addEventListener('click' , function(){
  short.className ='' ;
  mcq.className = '' ;


  short.className = 'chosen' ;
  document.getElementById('choice').value= 'short';
}) }
if (mcq != null) { 

mcq.addEventListener('click' , function(){
  short.className ='' ;
  mcq.className = '' ;


  mcq.className = 'chosen' ;
  document.getElementById('choice').value= 'mcq';
}) }






let err=0 ;
err = document.getElementsByClassName('errorlist nonfield');
if(err.length !== 0) {
    alert(err[0].innerText);
  }
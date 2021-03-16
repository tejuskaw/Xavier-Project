let viewed = document.getElementsByClassName('viewed');


function change(on , next , prev) {
    document.getElementById('view').innerHTML='Questions Viewed : '+viewed.length
    
    let c= 0 ;
    let text = document.getElementsByTagName('textarea') ;
    for (i = 0; i < text.length; i++) {
        if (text[i].value == ''){c=c+1 ;}
      }
    if( text.length != 0){
    document.getElementById('answered').innerHTML='Answered : '+(10-c)
    document.getElementById('to_be_answered').innerHTML='To be answered : '+c}


    
}


let next =  document.getElementById('next');
next.addEventListener('click',function(event){
    let on = document.getElementsByClassName('on')[0] ;
    if(parseInt(on.id)< 10){
    on.className = 'off viewed' ;
    document.getElementById(String(parseInt(on.id) + 1)).className = 'on viewed' ;
    

    change(on , next , prev) }

}) ;



let prev = document.getElementById('prev');
prev.addEventListener('click',function(event){
    let on = document.getElementsByClassName('on')[0] ;
    if(parseInt(on.id) > 1){
    on.className = 'off viewed' ;
    document.getElementById(String(parseInt(on.id) - 1)).className = 'on viewed' ;


    change(on , next , prev) }

}) ;



t=document.getElementById('time').className



var countDownDate = new Date(t).getTime();


// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = 3600000- (now - countDownDate) + 16200000 ;

  // Time calculations for days, hours, minutes and seconds
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  if (distance < 60) {
    document.getElementById("time").style.color = 'red';
  }
  
  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("time").innerHTML = "EXPIRED";
    document.getElementById('submit').click() ;
    return ;
  }
  document.getElementById("time").innerHTML =  minutes + "m " + seconds + "s ";


}, 1000);



let err=0 ;
err = document.getElementsByClassName('errorlist nonfield');
if(err.length !== 0) {
    alert(err[0].innerText);
  }




  document.querySelectorAll('.option').forEach(item => {
    item.addEventListener('click', event => {


      item.parentElement.childNodes[1].className = 'option a'
      item.parentElement.childNodes[3].className = 'option b'
      item.parentElement.childNodes[5].className = 'option c'
      item.parentElement.childNodes[7].className = 'option d'



      if(item.classList.length < 3 ) {
      item.className = item.className + ' chosen' }
      item.parentElement.parentElement.childNodes[5].value = item.classList[1]

      let ch = document.getElementsByClassName('chosen')
      console.log(ch)
    if( ch.length > 0) {
    
      document.getElementById('answered').innerHTML='Answered : '+ ch.length
      document.getElementById('to_be_answered').innerHTML='To be answered : '+(10-ch.length)
     }



    })
  })



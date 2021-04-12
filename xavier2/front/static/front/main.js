

let input = document.getElementById("id_content") ;
input.placeholder = 'send message' ;




input.addEventListener('keydown',function(event){
    if (event.keyCode==13){
        console.log(input.value) ;
        document.getElementById("send").click()   
    }  
}) ;
input.addEventListener('keyup',function(event){
    if (event.keyCode==13){
        input.value='' ;
          
    }  
}) ;





let err=0 ;
err = document.getElementsByClassName('errorlist nonfield');
if(err.length !== 0) {
    alert(err[0].innerText);
    document.getElementsByClassName('box')[0].className='box box2' ;
	}


const myBtn = document.getElementById('genBtn')
const myInput = document.getElementById('passwordBox')
const myText = document.getElementById('textShow') 


myBtn.addEventListener('click',async function(){
   try{
    const response = await fetch("/passhome");
    const data = await response.text()
    myInput.value = data
    myText.innerText = "your's password" + data

   }
   catch (error){
     console.log("error")
     myText.innerText = "server is not running"
   }
})
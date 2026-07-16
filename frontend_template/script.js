const myBtn = document.getElementById('genBtn')
const myInput = document.getElementById('passwordBox')
const myText = document.getElementById('textShow')
const password_length = document.getElementById('passLength')
const special_charactersAllow_or_not = document.getElementById('includeSymbols')




myBtn.addEventListener('click',async function(){
  try{
   const pass_len = parseInt(password_length.value) || 10
   if(pass_len > 32 ){
    myInput.value = ""
    myText.innerText = "do not write  greather then 32 "
    return
   }
   if(pass_len < 6){
    myInput.value = ""
    myText.innerText = "do not write password less then 6"
    return
   }
    
    const datapackets = {
      pass_len : pass_len,
      special_char : special_charactersAllow_or_not.checked,

    }
    const response = await fetch('/passhome',{
      method:'POST',
      headers:{
           'content-type':"application/json"
      },
      body: JSON.stringify(datapackets),

      
    })
    
    const data  = await response.json()
    console.log(data)
    if (data.password.startsWith("Error:")) {
      myInput.value = ""
      myText.innerText = data.password
      return
    }
    
    
    myInput.value = data.password
    myText.innerText = data.password
  }
  catch(error){
        console.log(error)
        myText.innerText = "server is not responding "
  }
})
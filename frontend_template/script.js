const myBtn = document.getElementById('genBtn')
const myInput = document.getElementById('passwordBox')
const myText = document.getElementById('textShow')
const password_length = document.getElementById('passLength')
const special_charactersAllow_or_not = document.getElementById('includeSymbols')




myBtn.addEventListener('click',async function(){
  try{
    const datapackets = {
      pass_len : parseInt(password_length.value) || 10,
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
    myInput.value = data.password
    myText.innerText = data.password
  }
  catch(error){
        console.log("error")
        myText.innerText = "server is not responding "
  }
})


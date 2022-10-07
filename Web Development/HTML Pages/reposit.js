function hobbySubmit() 
    {
      let text;
       
        text = "Your response is ";
        if(hobby1.checked==true)
        {
            text=text+" Reading"
        } 
        if(hobby2.checked==true)
        {
            text=text+" Singing"
        }
        if(hobby3.checked==true)
        {
            text=text+" Writing"
        }
        if(hobby4.checked==true)
        {
            text=text+" Travelling"
        }
        if(hobby5.checked==true)
        {
            text=text+" Cycling"
        }
    
        confirm("Do you want to submit:    "+text)
      document.getElementById("p1").innerHTML = text;
    }
    
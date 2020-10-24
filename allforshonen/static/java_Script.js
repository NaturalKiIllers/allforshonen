
//Funciones de La pág. Contacto. 
function validarContacto(){
 
    var nombre=document.getElementById("nombres");
    var correo=document.getElementById("correo");
    var asunto=document.getElementById("input_text");
    var mensaje=document.getElementById("textarea1");
 
    //Test campo obligatorio
    if(nombre.value == "") {
      alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
      nombre.focus();
      return false;
    }else if(correo.value == ""){
      alert('ERROR: Debe escribir un correo válido');
      return false;
    }else if(asunto.value == ""){
        alert('ERROR: El campo asunto no debe ir vacío o lleno de solamente espacios en blanco');
        return false;
    }else if(mensaje.value == ""){
        alert('ERROR: El campo mensaje no debe ir vacío o lleno de solamente espacios en blanco');
        return false;
    }else{
          alert("Todo Completado");
    return true;
    }
  }

//Solo letras
function soloLetras(e) {
    var key = e.keyCode || e.which,
      tecla = String.fromCharCode(key).toLowerCase(),
      letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
      especiales = [8, 37, 39, 46],
      tecla_especial = false;

    for (var i in especiales) {
      if (key == especiales[i]) {
        tecla_especial = true;
        break;
      }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
      return false;
    }
  }
//Solo numeros
  function soloNumeros(e){
	var key = window.Event ? e.which : e.keyCode
	return (key >= 48 && key <= 57 || key==43) 

  }
//Funciones de la pág. Registrarse. 

function revisarForm()
{
    var nombre =document.getElementById("nombre");
    var apellido =document.getElementById("apellido");
    var direccion =document.getElementById("direccion");
    var region =document.getElementById("region");
    var correo =document.getElementById("correo");
    var telefono =document.getElementById("telefono");
    var contraseña =document.getElementById("contraseña");
    var contraseñaR =document.getElementById("contraseñaR");
   
        if(nombre.value=="")
        {
            alert("ERROR: El campo nombre no debe estar vacío");
            nombre.focus();  
            return false;     
        }else if(apellido.value=="")
        {
            alert("ERROR: El campo apellido no debe estar vacío");
            apellido.focus()
            return false;
        }else if(direccion.value=="")
        {
            alert("ERROR: El campo dirección no debe estar vacío");
            direccion.focus();
            return false;
        }else if(region.selectedIndex==0)
        {
            alert("ERROR: El campo región no debe estar vacío");
            region.focus();
            return false;
        }else if(correo.value=="")
        {
            alert("ERROR: El campo correo no debe estar vacío");
            correo.focus();
            return false;   
        }else if(telefono.value=="")
        {
            alert("ERROR: El campo telefono no debe estar vacío");
           
            return false;   
        }
        else if(contraseña.value=="")
        {
            alert("ERROR: El campo contraseña no debe estar vacío");
            contraseña.focus();
            return false;
        }else if(contraseñaR.value=="")
        {
            alert("ERROR: El confirmación contraseña no debe estar vacío");
            
            return false;
        }else{
          alert("Ahora eres parte de All For Shonen, "+nombre.value+".")
        return true;
        }


}


 //TODO:Contraseñas iguales 

 function igualpassword(){

  var contraseña=document.getElementById("contraseña");
  var contraseñaR=document.getElementById("contraseñaR");
  if(contraseña.value !=contraseñaR.value)
  {
      
    
      alert("Por favor, revise las contraseñas no son iguales");
     
     
  }
  else{      
  }
}


function cadenanumero(){
  var telefono=document.getElementById("telefono").value;
  if(telefono.length=="12")
  {
    
     
  }
  else{
      alert("Por favor, revise su numero de telefono nuevamente");
     
  }
}





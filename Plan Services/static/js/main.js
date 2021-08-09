history.forward()

function Edad() {
    const fecha_nacimiento = document.getElementById("date-picker").value;
    var fechaNace = new Date(fecha_nacimiento);
    var fechaActual = new Date()
    var mes = fechaActual.getMonth();
    var dia = fechaActual.getDate();
    var año = fechaActual.getFullYear();
    fechaActual.setDate(dia);
    fechaActual.setMonth(mes);
    fechaActual.setFullYear(año);
    edad = Math.floor(((fechaActual - fechaNace) / (1000 * 60 * 60 * 24) / 365));
    if (edad < 18) {
        swal("Esta persona debe ser mayor de edad")
        return document.getElementById("date-picker").value = null;
    }
}

/* VALIDACIÓN DE CARACTERES */

function SoloLetras(e){
    key = e.keyCode || e.wich;
    tecla = String.fromCharCode(key).toString();
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú"
    especiales = [8, 13, 32];
    tecla_especial = false;
    for(var i in especiales){
        if(key == especiales[i]){
            tecla_especial = true;
            break;
        }
    }
    if(letras.indexOf(tecla) == -1 && !tecla_especial){
        swal("Ingresar solo letras")
        return false;
    }
}

function SoloNumeros(evt){
    if(window.event){
        keynum = evt.keyCode;
    }else{
        keynum = evt.wich;
    }
    if(keynum > 47 && keynum < 58 || keynum == 8 || keynum == 13){
        return true;
    }else{
        swal("Ingresar solo números")
        return false;
    }
}

/* BOTÓN DE ELIMINAR DATOS */

const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Está seguro que desea eliminar esto?')){
                e.preventDefault();
            }
        })
    });
}

/* BOTÓN DE EDITAR DATOS */

const btnEdit = document.querySelectorAll('.btn-edit')

if (btnEdit){
    const btnArray = Array.from(btnEdit);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Está seguro que desea editar esto?')){
                e.preventDefault();
            }
        })
    });
}
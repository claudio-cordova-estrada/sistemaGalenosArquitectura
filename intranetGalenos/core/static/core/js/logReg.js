function registrarUsuario() {
    // Obtener los valores del formulario
    var username = document.getElementById("nombre").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var apellido_paterno = document.getElementById("apellido_paterno").value;
    var apellido_materno = document.getElementById("apellido_materno").value;
    var telefono = document.getElementById("telefono").value;


    // Validar los campos (puedes agregar más validaciones según tus necesidades)
    if (username === "" || password === "" || email === "" || 
    apellido_paterno === "" || apellido_materno === "" || telefono === "") {
        alert("Por favor, completa todos los campos.");
        return;
    }

    // Enviar los datos al servidor (puedes usar AJAX, Fetch, etc.)
    fetch('logReg', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Agrega el token CSRF para protección
        },
        body: JSON.stringify({
            nombre: username,
            email: email,
            password: password,
            apellido_paterno: apellido_paterno,
            apellido_materno: apellido_materno,
            telefono: telefono,
            rutCliente: rutCliente,
            direccion: direccion,
        }),
    })

    .then(response => response.json())
    .then(data => {
        // Manejar la respuesta del servidor (redireccionar, mostrar mensajes, etc.)
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Buscar la cookie con el nombre especificado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
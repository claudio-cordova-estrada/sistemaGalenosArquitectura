function registrarUsuario() {
    // Obtener los valores del formulario
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Validar los campos (puedes agregar más validaciones según tus necesidades)
    if (nombre === "" || email === "" || password === "") {
        alert("Por favor, completa todos los campos.");
        return;
    }

    // Procesar la información (puedes enviarla a un servidor, almacenarla en localStorage, etc.)
    // En este ejemplo, simplemente mostramos un mensaje de éxito en la consola.
    console.log("Usuario registrado con éxito:");
    console.log("Nombre: " + nombre);
    console.log("Correo Electrónico: " + email);
    // ¡No debes almacenar contraseñas en texto plano! En un entorno real, deberías usar algún método de cifrado.

    // Puedes redirigir al usuario a otra página después del registro si lo deseas.
    // window.location.href = "pagina-exito.html";
}
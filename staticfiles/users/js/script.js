document.querySelector('#signup').addEventListener('submit', function(form) {
    form.preventDefault();

    const password1 = document.querySelector("#id_password1");
    const password2 = document.querySelector("#id_password2");
    const message = document.querySelector(".error-message");
    message.innerHTML = "";

    if (password1.value!== password2.value) {
        message.innerHTML = "Passwords do not match";
        return;
    } else if (password1.value.length < 8) {
        message.innerHTML = "Password should have atleast 8 characters";
        return;
    } else {
        form.submit();
    };
});
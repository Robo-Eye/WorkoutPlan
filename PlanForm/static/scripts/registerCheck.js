// listener for when document loads
window.addEventListener("DOMContentLoaded", function() {
    // get password fields
    let pass = document.getElementById("pass");
    let confPass = document.getElementById("confPass");

    // if change in either field, check to see if the password are the same and if it meets length requirements
    pass.addEventListener("change", checkPassword);
    confPass.addEventListener("change", checkPassword);
});

function checkPassword(){
    // get fields
    let pass = document.getElementById("pass");
    let confPass = document.getElementById("confPass");

    // if not long enough
    if (pass.value.length < 8){
        pass.setCustomValidity("Password needs to be 8 or more characters");
    }
    // if too long
    else if (pass.value.length > 256){
        pass.setCustomValidity("Password cannot be more than 256 characters");
    }else{
        pass.setCustomValidity("");
    }

    // if they are equal
    if (pass.value === confPass.value){
        confPass.setCustomValidity("");
    }
    // if they are not equal
    else{
        // tell user they don't match
        confPass.setCustomValidity("Passwords do not match");
    }


}


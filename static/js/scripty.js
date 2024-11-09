/** created for Python learning Project #5 **/

$(document).ready(function () {
    console.log("Loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function (event) {
        event.preventDefault();

        let form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
            }
        })
    });

    $(document).on("submit", "#login-form", function (event) {
        event.preventDefault();
        let form = $('#login-form').serialize();
        $.ajax({
            url: '/checklogin',
            type: 'POST',
            data: form,
            success: function (response) {
                if (response == "error") {
                    console.log("Login failed", response);
                }
                else {
                    console.log("Login successful", response);
                    window.location.href = '/';
                }
            }
        })

    })

    $(document).on("click", "#logout-link", function (event) {
        event.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function (response) {
                console.log(response);
                if (response == "Success") {
                    window.location.href = '/login';
                }
                else {
                    console.log("Logout error", response);
                }
            }
        })
    })

    $(document).on("submit", "#post-activity", function (event) {
        event.preventDefault();
        form = $('#post-activity').serialize();

        $.ajax({
            url: '/postactivity',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
            }
        })
    })

    $(document).on("submit", "#settings-form", function (event) {
        event.preventDefault();
        let form = $('#settings-form').serialize();

        $.ajax({
            url: '/update-settings',
            type: 'POST',
            data: form,
            success: function (response) {
                if (response == "Success") {
                    window.location.href = '/';
                }
                else {
                    alert(response);
                }
            }
        })
    })

    $(document).on("submit", "#avatar-upload", function (event) {
        event.preventDefault();
        let form = $('#avatar-upload').serialize();

        $.ajax({
            url: '/upload-avatar',
            type: 'POST',
            data: form,
            success: function (response) {
                if (response == "Success") {
                    window.location.href = '/';
                }
                else {
                    alert(response);
                }
            }
        })
    })
});



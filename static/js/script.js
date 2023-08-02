// Flash message for successfully changing password for user //

document.addEventListener('DOMContentLoaded', function () {
    var flashMessages = document.querySelectorAll('.alert-success');
    flashMessages.forEach(function (message) {
        setTimeout(function () {
            message.style.display = 'none';
        }, 5000); // 5000 milliseconds (5 seconds)
    });
});



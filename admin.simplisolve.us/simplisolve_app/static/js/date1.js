$(document).ready(function () {
    $(".invite-link").click(function (e) {
        e.preventDefault();
        $(this).siblings(".invite-form").toggle();
    });
});

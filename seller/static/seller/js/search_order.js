$(document).ready(function () {
    $("#search-order-btn").click(function () {
        let uuid = $("#id_uuid").val();
        console.log(uuid)
        let url = `/api/orders/${uuid}/`;

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                console.log(data);
                window.location.href = `/orders/${uuid}/`;
            },
            error: function (xhr) {
                console.log("error")
            }
        });
    });
});
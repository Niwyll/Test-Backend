$(document).ready(function () {
    $("#search-order-btn").click(function () {
        let uuid = $("#id_uuid").val();
        let url = `/api/orders/${uuid}/`;

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                console.log(data)
            },
            error: function (xhr) {
                console.log("error")
            }
        });
    });
});
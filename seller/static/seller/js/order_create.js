$(document).ready(function () {
    function getCSRFToken() {
        let csrfCookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
        return csrfCookie ? csrfCookie.split("=")[1] : "";
    }

    const icecreams_url = "/api/icecreams/";
    let flavours = []
    $.ajax({
        url: icecreams_url,
        type: "GET",
        success: function (data) {
            flavours = data.map(choice => {
                return [choice.name, choice.name.toLowerCase().replace(/\s+/g, "-"), 0];
            });  // Extract only the labels
        },
        error: function (xhr) {
            console.log("Api not found");
        }
    });

    $(".selectable-item").click(function () {
        let selectedFlavour = flavours.find(item => item[1] === $(this).attr('id'));
        selectedFlavour[2] += 1;

        let orderList = "<ul>";
        flavours.forEach(flavour => {
            orderList += `<li>${flavour[2]}X ${flavour[0]}</li>`;
        });
        orderList += "</ul>";
        $("#order-list").html(orderList)

        $("#create-order-button").prop('disabled', false);
    });

    const toastLiveExample = document.getElementById('liveToast');
    $("#create-order-button").click(function () {
        let formattedFlavours = flavours.reduce((acc, flavour) => {
            acc[flavour[0]] = flavour[2]; // Use the first element as the key and the third as the value
            return acc;
        }, {});
        $.ajax({
            url: '/api/orders/',
            type: "POST",
            contentType: "application/json",
            headers: { "X-CSRFToken": getCSRFToken() },
            data: JSON.stringify({ items: formattedFlavours }),
            success: function (data) {
                window.location.href = `/orders/${data.uuid}/confirm/`;
            },
            error: function (xhr) {
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
                console.log(JSON.parse(xhr.responseText).error)
                $('.toast-body').text(JSON.parse(xhr.responseText).error ?? JSON.parse(xhr.responseText).detail);
                toastBootstrap.show();
            }
        });
    });
});
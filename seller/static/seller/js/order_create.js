$(document).ready(function () {
    let url = "/api/icecreams/";
    let flavours = []
    $.ajax({
        url: url,
        type: "GET",
        success: function (data) {
            flavours = data.map(choice => {
                return [choice.name, choice.name.toLowerCase().replace(/\s+/g, "-"), 0];
            });  // Extract only the labels
            console.log(flavours);
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
    });

    $("#create-order-button").click(function () {
        let formattedFlavours = flavours.reduce((acc, flavour) => {
            acc[flavour[0]] = flavour[2]; // Use the first element as the key and the third as the value
            return acc;
        }, {});
        $.ajax({
            url: '/api/orders/  ',
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ items: formattedFlavours }),
            success: function (data) {
                console.log(data)
            },
            error: function (xhr) {
                console.log(xhr);
            }
        });
    });
});
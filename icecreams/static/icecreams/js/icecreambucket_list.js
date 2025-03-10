$(document).ready(function () {
    function getCSRFToken() {
        let csrfCookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
        return csrfCookie ? csrfCookie.split("=")[1] : "";
    }

    $(document).on("click", "[id^='refill-button-']", function() {
        let buttonId = this.id;
        let match = buttonId.match(/^refill-button-(\d+)$/);
        let $button = $(this); // Store button reference for callback
    
        if (match) {
            let bucketId = match[1];
            console.log("Refilling bucket with ID:", bucketId);
    
            $.ajax({
                url: `/api/icecreambuckets/${bucketId}/refill/`,
                type: "POST",
                contentType: "application/json",
                headers: { "X-CSRFToken": getCSRFToken() },
                success: function(response) {
                    location.reload();
                },
                error: function(xhr) {
                    console.log("Error refilling bucket:", xhr.responseText);
                }
            });
        }
    });
});
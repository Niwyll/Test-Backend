from django.urls import path, include

app_name = "icecreams"

urlpatterns = [
    path("api/", include("icecreams.api.urls")),
]
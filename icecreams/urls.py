from django.urls import path, include
from icecreams.views import ManagementBucketsView, ManagementRecipesView

app_name = "icecreams"

urlpatterns = [
    path("api/", include("icecreams.api.urls")),
    path("management/buckets/", ManagementBucketsView.as_view(), name="management-buckets"),
    path("management/recipes/", ManagementRecipesView.as_view(), name="management-recipes"),
]
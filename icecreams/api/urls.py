from django.urls import path
from icecreams.api.views import IceCreamListView

urlpatterns = [
    path("icecreams/", IceCreamListView.as_view(), name="list-icecreams"), 
]
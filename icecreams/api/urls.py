from django.urls import path
from icecreams.api.views import IceCreamListView, RefillBucketView

urlpatterns = [
    path("icecreams/", IceCreamListView.as_view(), name="list-icecreams"), 
    path("icecreambuckets/<int:bucket_id>/refill/", RefillBucketView.as_view(), name="refill-bucket")
]
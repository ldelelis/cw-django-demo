from buckets.views import BucketViewset
from rest_framework import routers

app_name = "buckets"

router = routers.SimpleRouter()
router.register('buckets', BucketViewset)

urlpatterns = router.urls

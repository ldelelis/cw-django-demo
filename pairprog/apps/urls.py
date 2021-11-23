from apps.views import AppViewset
from rest_framework import routers

app_name = "apps"

router = routers.SimpleRouter()
router.register('apps', AppViewset)

urlpatterns = router.urls

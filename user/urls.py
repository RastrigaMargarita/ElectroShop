from rest_framework import routers

from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
urlpatterns = router.urls

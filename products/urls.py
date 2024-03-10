from rest_framework import routers

from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet, basename="product")
urlpatterns = router.urls

from rest_framework import routers
from company.views import CountryViewSet, TownViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename="company")
urlpatterns = router.urls
router.register(r'countries', CountryViewSet, basename="country")
urlpatterns += router.urls
router.register(r'towns', TownViewSet, basename="town")
urlpatterns += router.urls

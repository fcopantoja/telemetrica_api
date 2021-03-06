from django.conf.urls import url, include
from rest_framework import routers
from restaurantes.views import RestauranteViewSet

router = routers.DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
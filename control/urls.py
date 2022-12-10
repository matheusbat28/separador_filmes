from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet, MovieViewSet, AverageViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'average', AverageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers

from api.views import ConsumerView


router = routers.DefaultRouter(trailing_slash=False)
router.register('consumers', ConsumerView, basename='consumer')

urlpatterns = [
    path('', include(router.urls))
]

from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ApiView

router = DefaultRouter()
router.register("api", ApiView)

urlpatterns = [
    path("", include(router.urls))
]

from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls), name="list")
]

app_name = "author"

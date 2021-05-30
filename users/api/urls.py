from django.urls import path, include
from rest_framework import routers

from users.api.views import AccountViewSet, UserViewSet

router = routers.DefaultRouter()

router.register("signup", UserViewSet, basename="signup")
# router.register("accounts", AccountViewSet, basename="account")

urlpatterns = [
    path('', include(router.urls)),
]
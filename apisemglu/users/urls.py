from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/login/",
        views.CustomObtainTokenPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", views.RegisterView.as_view(), name="auth_register"),
    path("api/logout/", views.LogoutView.as_view(), name="logout"),
]

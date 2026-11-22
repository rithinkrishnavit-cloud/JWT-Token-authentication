from django.urls import path
from . import views

# `TokenObtainPairView` is a built-in view already available in Simple JWT.

# It performs the following steps:
# 1. Accepts the username.
# 2. Accepts the password.
# 3. Verifies the user credentials.
# 4. Generates an access token.
# 5. Generates a refresh token.
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("register/", views.register, name="register"),
    # JWT Login
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("profile/", views.profile, name="profile"),
]

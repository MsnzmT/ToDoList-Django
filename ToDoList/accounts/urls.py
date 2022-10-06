from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from accounts.views import *


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutJWT.as_view()),
    path('signup/', SignUp.as_view()),
]
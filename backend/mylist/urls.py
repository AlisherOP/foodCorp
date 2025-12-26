"""
URL configuration for mylist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_views# importing login view for the site to have
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework import routers
from food.views import RoomView
from django.conf.urls.static import static
from django.conf import settings
#api for users
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('movies', RoomView, basename='movies')


urlpatterns = [
    #serialized version
    path("api/", include("api.urls")),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name= "get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name= "refresh"),
    path("api-auth/", include("rest_framework.urls")),

    path('ap/', include(router.urls)),

    path('admin/', admin.site.urls),
    path("food/", include("food.urls")),
    path("register/", user_views.register, name="register"),
    path("login/", authentication_views.LoginView.as_view(template_name="users/login.html"), name= "login"),#for as view: the place wher you should search for the tamplate
    path("logout/", authentication_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("users/", include("users.urls")),
    path("profile/",  user_views.profilepage, name= "profile"),
    path("fav/<int:id>/", user_views.favourite_add, name="favourite_add"),
    path("profile/favourites/", user_views.favourite_list, name='favourite_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

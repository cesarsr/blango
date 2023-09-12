from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from blog.api.views import UserDetail, TagViewSet, PostViewSet


router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),

    path("", include(router.urls)),
]

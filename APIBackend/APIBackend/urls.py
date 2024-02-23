from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.users import views as UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.projects import views as PView
router = DefaultRouter()
router.register('users',UserView.UserViewSet)
router.register('projects',PView.ProjectViewSet)
router.register('tasks',PView.TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Api
    path('api/v1/',include(router.urls)),
    path('api/v1/users/profile',UserView.UserProfileViewSet.as_view())    
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('university_api.apps.users.urls')),
    path('api/rooms/', include('university_api.apps.rooms.urls')),
    path('api/maintenance/', include('university_api.apps.maintenance.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

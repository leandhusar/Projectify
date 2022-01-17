from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from projectify.views.project_views import ProjectAPI
from projectify.views.report_views import ReportAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/project/', ProjectAPI.as_view(), name='project'),
    path('api/report/', ReportAPI.as_view(), name='report')
]

from django.contrib import admin
from django.urls import path, include
# from fscohort.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("fscohort.urls")),
    path('api/', include('fscohort_api.urls')),
]

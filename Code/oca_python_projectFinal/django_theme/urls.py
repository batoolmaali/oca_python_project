from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', admin.site.urls),
    path('', include('app.urls')), 
    # path('about/', include('app.urls')), 
    path('datatable/', include('app.urls')), 
    path('formdatatable/', include('app.urls')), 
    path('editdatatable/', include('app.urls')), 
    path('admin/', include('app.urls')), 
] 

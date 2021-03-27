from django.urls import path
from . import views
from app import views 
from django.contrib import admin  


urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('about/', views.about, name="about"),
    path('admin/', views.admin, name="admin"),
    path('datatable/', views.datatable, name="datatable"),
    path('formdatatable/', views.formdatatable, name="formdatatable"),
    path('editdatatable/', views.editdatatable, name="editdatatable"),

    # path('admin/', admin.site.urls),  
    path('signup', views.signup),  
    path('signout', views.signout),  
    path('signin', views.signin),  
    path('emp', views.emp),  
    path('simple_upload', views.simple_upload),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('single/<int:id>', views.single, name="single"),  
]
 

# https://localhost:8000/about/index.html


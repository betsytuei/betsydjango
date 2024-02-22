
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'homepage'),
    path('about/', views.about, name = 'about'),
    path('form/', views.form,name = 'formpage'),
    path('carousel/', views.carousel,name = 'carousel'),
]

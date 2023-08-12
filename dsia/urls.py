from django.contrib import admin
from django.urls import path, include
from app_one import views


urlpatterns = [
    path('', views.index, name="index-url"),
    path('admin/', admin.site.urls, name="admin-url"),
    path('about/', views.about, name="about-url"),
    path('contact/', views.contact, name="contact-url"),
    path('contact/<int:id>/<str:name>/', views.contact),
    path('about/v2/', views.AboutView.as_view(), name="about-v2-url"),
    path('api/v1/', include('api.urls')),
]

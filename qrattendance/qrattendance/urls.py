from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello),
    path("hi/", views.hi),
    path("qr/", views.qr),
    path("hlw/",views.hlw),
]
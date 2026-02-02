from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello),
    path("hi/", views.hi),
    path("qr/", views.qr),
    path("form/",views.form),
    path("data/",views.data),
    path("add/",views.add),
    path("result/",views.result),
]
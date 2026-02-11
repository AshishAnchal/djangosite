from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello),
    path("data/",views.data),
    path("result/",views.result),
    path("radio/",views.radio),
    path("open/",views.open),
    path("chek/",views.chek),
    path('now/',views.now),
    path('merge/',views.merge),
    path('form1',views.form1),
    path('check/',views.check),
    path('veg/',views.veg),
    path('sessionadd/',views.sessionadd),
    path('sessionremove/',views.sessionremove),
    path('sessionview/',views.sessionview),
    path('dologin/',views.dologin),
    path('protected/',views.protected),
    path('dologout/',views.dologout),
]
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^new/', views.NewUserForm, name="New User"),
]
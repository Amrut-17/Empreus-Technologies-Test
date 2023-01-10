from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path("create/", views.create, name="create"),
    path("add/", views.add_event, name='add'),
]

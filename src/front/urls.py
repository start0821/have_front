from django.urls import path
from . import views

urlpatterns = [
    path('list',views.list,name='list'),
    path('list/<int:name>',views.list,name='list_name'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'), 
    path('index/<list_id>', views.delete, name='delete'),
    path('cross/<list_id>', views.cross, name = 'cross'),
    path('uncross/<list_id>', views.uncross, name = 'uncross'),
]
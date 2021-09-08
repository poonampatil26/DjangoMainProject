from django.urls import path
from .views import add, update, delete, show, home

urlpatterns = [
    path('add/',add, name = 'add'),
    path('show/', show, name='show'),
    path('update/<int:id_f>/', update, name = 'update'),
    path('delete/<int:id_f>/', delete, name = 'delete'),
    path('home/', home, name='home'),

]
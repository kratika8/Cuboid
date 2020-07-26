from django.urls import path
from . import views, api

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='site_index'),
    path('add', views.create_view, name='site_index'),
    path('register', views.register, name='site_index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('list', views.list_view, name='Cars'),
    path('particular/<id>', views.detail_view, name='particular'),
    path('update/<id>', views.update_view, name='particular'),
    path('delete/<id>', views.delete_view, name='delete'),
    ]
    

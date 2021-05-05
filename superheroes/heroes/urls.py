from . import views
from django.urls import path

app_name = 'heroes'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create_hero, name='create_hero'),
    path('edit/<int:hero_id>', views.edit_hero, name='edit_hero'),
    path ('delete/<int:hero_id>/', views.delete_hero, name='delete')

]

from . import views
from django.urls import path

app_name = 'heroes'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail')
]

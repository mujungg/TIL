from django.urls import path
from . import views   # 현재 디렉토리에서 views.py를 import

urlpatterns = [
    path('', views.index, name='index'),
]
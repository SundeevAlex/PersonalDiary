from django.urls import path

from diary.apps import DiaryConfig
from diary.views import diary_list, diary_detail

app_name = DiaryConfig.name

urlpatterns = [
    path('', diary_list, name='diary_list'),
    path('diary/<int:pk>/', diary_detail, name='diary_detail'),
]

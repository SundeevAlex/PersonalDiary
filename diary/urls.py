from django.urls import path

from diary.apps import DiaryConfig
from diary.views import diary_list

app_name = DiaryConfig.name

urlpatterns = [
    path("", diary_list, name="diary_list"),
]

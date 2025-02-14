from django.urls import path

from diary.apps import DiaryConfig
from diary.views import (DiaryCreateView, DiaryDeleteView, DiaryDetailView,
                         DiaryListView, DiaryUpdateView, SearchResultsView)

app_name = DiaryConfig.name

urlpatterns = [
    path("", DiaryListView.as_view(), name="diary_list"),
    path("diary/<int:pk>/", DiaryDetailView.as_view(), name="diary_detail"),
    path("diary/create", DiaryCreateView.as_view(), name="diary_create"),
    path("diary/<int:pk>/update/", DiaryUpdateView.as_view(), name="diary_update"),
    path("diary/<int:pk>/delete/", DiaryDeleteView.as_view(), name="diary_delete"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]

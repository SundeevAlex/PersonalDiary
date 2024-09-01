from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary


class DiaryDetailView(DetailView):
    model = Diary


class DiaryCreateView(CreateView):
    model = Diary
    fields = ('author', 'created_at', 'topic', 'image_cover', 'content', 'image', 'place')
    success_url = reverse_lazy('diary:diary_list')


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ('author', 'topic', 'image_cover', 'content', 'image', 'place')
    success_url = reverse_lazy('diary:diary_list')


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

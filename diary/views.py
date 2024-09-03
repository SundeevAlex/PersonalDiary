from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary


class DiaryDetailView(DetailView):
    model = Diary


class DiaryCreateView(CreateView, LoginRequiredMixin):
    model = Diary
    fields = ('author', 'created_at', 'topic', 'image_cover', 'content', 'image', 'place')
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save()
        user = self.request.user
        diary.author = user
        diary.save()
        return super().form_valid(form)

class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ('author', 'topic', 'image_cover', 'content', 'image', 'place')
    success_url = reverse_lazy('diary:diary_list')


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

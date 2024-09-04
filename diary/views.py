from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary


class SearchResultsView(ListView):
    model = Diary
    success_url = reverse_lazy("diary:search_results")

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Diary.objects.filter(
            Q(topic__icontains=query)
            | Q(content__icontains=query)
            | Q(place__icontains=query)
        )
        return object_list


class DiaryDetailView(DetailView):
    model = Diary


class DiaryCreateView(CreateView, LoginRequiredMixin):
    model = Diary
    fields = ("created_at", "topic", "image_cover", "content", "image", "place")
    success_url = reverse_lazy("diary:diary_list")

    def form_valid(self, form):
        diary = form.save()
        user = self.request.user
        diary.author = user
        diary.save()
        return super().form_valid(form)


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ("author", "topic", "image_cover", "content", "image", "place")
    success_url = reverse_lazy("diary:diary_list")


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy("diary:diary_list")

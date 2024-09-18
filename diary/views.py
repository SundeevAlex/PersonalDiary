from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from diary.models import Diary


class DiaryListView(ListView):
    """ Просмотр списка записей в дневнике """

    model = Diary

    def get_queryset(self):
        queryset = Diary.objects.order_by('-created_at', 'topic')
        return queryset


class SearchResultsView(ListView):
    """Поиск записей в дневнике """

    model = Diary
    success_url = reverse_lazy("diary:search_results")

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Diary.objects.filter(
            Q(topic__icontains=query)
            | Q(content__icontains=query)
            | Q(place__icontains=query)
            | Q(created_at__icontains=query)
            | Q(updated_at__icontains=query)
        )
        return object_list


class DiaryDetailView(DetailView):
    """ Просмотр одной записи в дневнике """

    model = Diary


class DiaryCreateView(CreateView, LoginRequiredMixin):
    """ Создание записи в дневнике """

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
    """ Редактирование записи в дневнике """

    model = Diary
    fields = ("topic", "image_cover", "content", "image", "place")
    success_url = reverse_lazy("diary:diary_list")


class DiaryDeleteView(DeleteView):
    """ Удаление записи из дневника """

    model = Diary
    success_url = reverse_lazy("diary:diary_list")

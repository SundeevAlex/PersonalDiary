from django.shortcuts import render

from diary.models import Diary


def diary_list(request):
    records = Diary.objects.all()
    context = {"record": records}
    return render(request, "diary/diary_list.html", context)

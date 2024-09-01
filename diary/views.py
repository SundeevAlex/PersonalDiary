from django.shortcuts import render, get_object_or_404

from diary.models import Diary


def diary_list(request):
    records = Diary.objects.all()
    context = {"record": records}
    return render(request, "diary/diary_list.html", context)


def diary_detail(request, pk):
    # record = Diary.objects.get(pk=pk)
    record = get_object_or_404(Diary, pk=pk)
    context = {"record": record}
    return render(request, "diary/diary_detail.html", context)

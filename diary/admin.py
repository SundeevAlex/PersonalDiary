from django.contrib import admin

from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic")
    list_filter = (
        "topic",
        "place",
    )
    search_fields = (
        "topic",
        "place",
    )

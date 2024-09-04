from django.db import models

from users.models import User

NULLABLE = {"blank": "True", "null": "True"}


class Diary(models.Model):
    author = models.ForeignKey(
        User, verbose_name="Автор", **NULLABLE, on_delete=models.SET_NULL
    )
    created_at = models.DateField(
        auto_created=True, verbose_name="Дата создания", **NULLABLE
    )
    updated_at = models.DateField(
        auto_now_add=True, verbose_name="Дата изменения", **NULLABLE
    )
    topic = models.CharField(
        max_length=50, verbose_name="Тема/заголовок", help_text="Введите тему/заголовок"
    )
    image_cover = models.ImageField(
        upload_to="diary/photo/cover",
        verbose_name="Фото обложки",
        help_text="Загрузите фото обложки",
        **NULLABLE,
    )
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите текст вашего дневника"
    )
    image = models.ImageField(
        upload_to="diary/photo",
        verbose_name="Фото события",
        help_text="Загрузите фото события",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=50, verbose_name="Место", help_text="Введите место события"
    )

    class Meta:
        verbose_name = "Дневник"
        verbose_name_plural = "Дневники"
        ordering = ["-created_at", "topic"]

    def __str__(self):
        return f"{self.topic} {self.content} {self.author}"

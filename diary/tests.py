from django.test import TestCase
from diary.models import Diary
from users.models import User


class DiaryTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.habits = Diary.objects.create(
            author=self.user,
            topic="Weekends",
            content="Best",
            place="Altay",
        )

    def test_diary_create(self):
        Diary.objects.create(topic="The", content="Text", place="There")
        diary_count = Diary.objects.all().count()
        self.assertEqual(diary_count, 2)

    def test_diary_list(self):
        diary_count = Diary.objects.all().count()
        self.assertEqual(diary_count, 1)

    def test_diary_detail(self):
        diary = Diary.objects.get(topic="Weekends")
        self.assertEqual(diary.content, "Best")
        self.assertEqual(diary.place, "Altay")

    def test_diary_update(self):
        diary = Diary.objects.get(topic="Weekends")
        diary.content = "No best"
        self.assertEqual(diary.content, "No best")

    def test_diary_delete(self):
        diary = Diary.objects.get(topic="Weekends")
        diary.delete()
        diary_count = Diary.objects.all().count()
        self.assertEqual(diary_count, 0)

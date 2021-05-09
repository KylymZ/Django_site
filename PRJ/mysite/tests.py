from django.test import TestCase
import datetime
from django.utils import timezone
from .models import NEWS
class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = NEWS(date=time)
        self.assertEqual(future_question.was_published_recently(), False)

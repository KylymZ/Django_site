from django.db import models
import datetime
from django.utils import timezone
class NEWS(models.Model):
    name=models.CharField('Автор статьи',max_length=100,default='Женишбеков К')
    title=models.CharField('Название',max_length=100)
    text=models.TextField('Текст статьи')
    date=models.DateTimeField('Дата публикации',editable=False)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
    
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = NEWS(date=time)
        self.assertEqual(old_question.was_published_recently(), False)
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = NEWS(date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
    
def __unicode__(self):
    return self.title


class Meta:
    verbose_name= 'Новость'
    verbose_name_plural= 'Новости'


class Comment(models.Model):
    author_name=models.CharField('Имя автора', max_length=50)
    com_text=models.TextField('Текст комментария')


class Meta:
    verbose_name= 'Комментарий'
    verbose_name_plural= 'Комментарии'

def __unicode__(self):
    return self.author_name

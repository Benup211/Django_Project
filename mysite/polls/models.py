from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200);
    pub_text=models.DateTimeField('date published');

    def __str__(self):
        return self.question_text;
    def published_date(self):
        return self.pub_text>=timezone.now()-datetime.timedelta(days=1);

class choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE);
    choice_text=models.CharField(max_length=200);
    votes=models.IntegerField(default=0);

    def __str__(self):
        return self.choice_text;

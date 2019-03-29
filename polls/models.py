import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # question_text will be a column in the DB
    pub_date = models.DateTimeField('date published') # 'date published' is set as a human-readable name

    def __str__(self):
        return self.question_text # adds a String representation of a Question

    def was_published_recently(self):
        # Checks if the question was added in the last 24 hours.
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # sets a relationship with a Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text # adds a String representation of a Choice


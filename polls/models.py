from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # question_text will be a column in the DB
    pub_date = models.DateTimeField('date published') # 'date published' is set as a human-readable name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # sets a relationship with a Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


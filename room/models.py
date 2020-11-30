from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=10000)
    key_words = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    ans_count = models.IntegerField(default=0)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=10000)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def top_answers(self):
        return self.objects.order_by('-votes')[:5]

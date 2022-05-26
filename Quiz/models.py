from django.db import models
from django.db import connections

class Answer(models.Model):
    ans = models.CharField(default="", max_length=100,null=True,blank=True)

class Question(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + "번 문제"

class EndUser(models.Model):
    name = models.CharField(max_length=30, default="익명")
    answer = models.CharField(default="", max_length=10, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['score','name']

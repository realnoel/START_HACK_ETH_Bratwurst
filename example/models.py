from django.db import models
from django.contrib.auth.models import User

class Fund(models.Model):
    name = models.CharField(max_length=200)

class Question(models.Model):
    text = models.CharField(max_length=200)

class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    fund_impact = models.ManyToManyField(Fund, through='FundImpact')

class FundImpact(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    impact = models.IntegerField()

class UserFundsResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
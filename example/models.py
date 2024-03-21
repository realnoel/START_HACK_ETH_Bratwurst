from django.db import models
from django.contrib.auth.models import User
class Fund(models.Model):
    valor = models.CharField(max_length=200)
    isin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    domicile = models.CharField(max_length=200)
    gge = models.CharField(max_length=200)
    oil = models.CharField(max_length=200)
    acab = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    cannabis = models.CharField(max_length=200)

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
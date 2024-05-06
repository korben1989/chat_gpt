from django.db import models

class Answers(models.Model):
    user_cookies = models.CharField(max_length=1000)
    a2 = models.CharField(max_length=1000)
    q2 = models.CharField(max_length=1000)

class Answers1(models.Model):
    user_cookies = models.CharField(max_length=1000)
    a2 = models.CharField(max_length=1000)
    q2 = models.CharField(max_length=1000)

class Answers2(models.Model):
    user_cookies = models.CharField(max_length=1000)
    a2 = models.CharField(max_length=1000)
    q2 = models.CharField(max_length=1000)

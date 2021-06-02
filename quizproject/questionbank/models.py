from django.db import models

# Create your models here.
class qbank(models.Model):
    qus= models.CharField(max_length=150)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)
    op4 = models.CharField(max_length=150)
    ans = models.CharField(max_length=150)


    def __str__(self):
        return self.qus

class PythonQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)


    def __str__(self):
        return self.question

class DjangoQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)


    def __str__(self):
        return self.question

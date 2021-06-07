from django.db import models

#model for python
class PythonQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question


#model for django
class DjangoQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question


#model for quantitative
class QuantitativeQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question


#model for java
class JavaQBank(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question

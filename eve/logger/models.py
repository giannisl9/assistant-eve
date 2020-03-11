from django.db import models

class Subject(models.Model):
    PROGRAMMING = 'PGM'
    MATHEMATICS = 'MTH'
    PHYSICS = 'PHY'
    CIRCUITS_AND_ELECTRONICS = 'CAE'
    CATEGORY_CHOICES = [
            (PROGRAMMING, 'Programming'),
            (MATHEMATICS, 'Mathematics'),
            (PHYSICS, 'Physics'),
            (CIRCUITS_AND_ELECTRONICS, 'Circuits and Electronics')
    ]

    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.CharField(
            max_length=3,
            choices=CATEGORY_CHOICES,
    )

class Entry(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField()
    notes = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

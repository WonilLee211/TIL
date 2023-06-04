from django.db import models

# Create your models here.
class Either(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.CharField(max_length=10)
    issue_b = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Comment(models.Model):
    CHOICES = (
        ('issue_a', "Blue"),
        ('issue_b', "Red"),
    )
    pick = models.CharField(max_length=7, default="Blue", choices=CHOICES)
    content = models.CharField(max_length = 30)
    either = models.ForeignKey(Either, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    
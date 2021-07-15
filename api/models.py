from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

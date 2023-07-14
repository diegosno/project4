from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='user_pictures')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    

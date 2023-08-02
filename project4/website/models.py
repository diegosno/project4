from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class New(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("new-detail", kwargs={"pk": self.pk})
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='user_pictures')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.picture.path)
        
        if img.width > 500 or img.height > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.picture.path)
    
    

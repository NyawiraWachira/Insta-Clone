from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()

        
    def __str__(self):
        return f'{self.user.username} Profile'
    
    

# class Image(models.Model):
#     image = models.ImageField(null=False, blank=False)
#     image_name = models.CharField(max_length =30)
#     image_caption = models.TextField()
#     profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
#     post_date = models.DateTimeField(auto_now_add=True)
    # likes=
    # comments=

    

    # def __str__(self):
    #     return self.image_name

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField()

        
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)   


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

# def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # def save_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    # def save(self):
    #     super().save()

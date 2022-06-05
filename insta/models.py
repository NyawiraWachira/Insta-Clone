from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    bio = models.TextField()

def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()
    
    

    def __str__(self):
        return self.bio


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

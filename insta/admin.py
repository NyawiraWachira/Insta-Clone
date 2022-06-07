from django.contrib import admin
from.models import Profile,Post,Tag,Follow, Stream

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post) 
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)
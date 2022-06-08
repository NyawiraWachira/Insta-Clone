from django.test import TestCase
from .models import Post,Profile

# Create your tests here.
class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.working= Post( caption ='working', posted ='2022-June-7 3:00pm',likes='5', picture='default.png')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.working,Post))

        # Testing Save Method
    def test_save_method(self):
       self.working.save_post()
       all_objects = Post.objects.all()
       self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        filtered_object = Post.objects.filter(caption='working')
        Post.delete_post(filtered_object)
        all_objects = Post.objects.all()
        self.assertTrue(len(all_objects) == 0)
    
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.abigail= Profile(profile_photo='default.png', bio='Hey There, I am using insta!',)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abigail,Profile))

        # Testing Save Method
    def test_save_method(self):
       self.abigail.save()
       all_objects = Profile.objects.all()
       self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        filtered_object = Post.objects.filter(caption='working')
        Post.delete_post(filtered_object)
        all_objects = Post.objects.all()
        self.assertTrue(len(all_objects) == 0)
    

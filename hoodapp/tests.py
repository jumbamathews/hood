from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.profile = Profile(id=1, name='Tom Thomassen',user = self.user,bio='Bionic')
    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))


class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.post = Post(id=1,user = self.user,title='Title',content='Content')
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))


class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.post = Post(id=1,user = self.user,title='Title',content='Content')
        self.comment = Comment(id=1,post=self.post,user=self.user, comment= 'Comment test')
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))


class NeighborhoodTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.hood = Neighborhood(id=1,name='Corner',location="Dagoretti",occupants=1)
    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighborhood))
    # Test Create
    def test_create_neighborhood(self):
        self.hood.create_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) > 0)
    # Test Delete
    def test_delete_neighborhood(self):
        self.hood.create_neighborhood()
        self.hood = Neighborhood.objects.get(id=1)
        self.hood.delete_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) == 0)
    # Test Find
    def test_find_neighborhood(self):
        self.hood.create_neighborhood()
        self.searched_hood = Neighborhood.find_neighborhood(1)
        self.assertTrue(self.searched_hood == self.hood)
    # Test Update
    def test_update_neighborhood(self):
        self.hood.create_neighborhood()
        self.hood = Neighborhood.objects.get(id=1)
        self.hood.name = 'New name'
        self.hood.update_neighborhood()
        self.updated_hood = Neighborhood.objects.get(id=1)
        self.assertEqual(self.updated_hood.name,'New name')
    # Test Update Occupants
    def test_update_occupants(self):
        self.hood.create_neighborhood()
        self.hood = Neighborhood.objects.get(id=1)
        self.hood.update_occupants()
        self.updated_hood = Neighborhood.objects.get(id=1)
        self.assertTrue(self.updated_hood.occupants > 1)

class BusinessTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.profile = Profile(id=1, name='Tom Thomassen',user = self.user,bio='Bionic')
        self.hood = Neighborhood(id=1,name='Corner',location="Dagoretti",occupants=1)
        self.business = Business(id=1,name='Bizbiz',user=self.user,description='Description',neighborhood=self.hood,email='alpha@gmail.com')
        self.hood.save()
        self.business.save()
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
    # Test Create
    def test_create_business(self):
        self.business.create_business()
        self.assertTrue(len(Business.objects.all()) > 0)
    # Test Delete
    def test_delete_business(self):
        self.business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)
    # Test Find
    def test_find_business(self):
        self.business = Business.find_business(1)
        self.assertEqual(self.business.id, 1)
    # Test Update
    def test_update_business(self):
        self.business = Business.find_business(1)
        self.business.name = 'New name'
        self.business.update_business()
        self.updated_business = Business.find_business(1)
        self.assertEqual(self.updated_business.name, 'New name')

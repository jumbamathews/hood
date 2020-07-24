from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighborhood(models.Model):
    LOCATIONS = (
    ('Parklands','Nairobi',),
    ('highridge','Nairobi'),
    ('karen', 'Nairobi'),
    ('Mata', 'Nairobi'),
    ('Eastleigh', 'Nairobi'),
    )
    name = models.CharField(max_length = 30, null=True)
    hood_image = models.ImageField(upload_to='images/', null=True,blank=True)
    location = models.CharField(max_length=50,choices=LOCATIONS, null=True)
    occupants = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()



class Profile(models.Model):
    avatar = models.ImageField(upload_to='photos/',null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length = 50)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length = 60, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

    def __str__(self):
        return self.name



class Business(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()



class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']



class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.username} + {self.post}"

    class Meta:
        ordering = ['-pub_date']

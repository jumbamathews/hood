from django.contrib import admin
from .models import Neighborhood, Profile, Business, Post, Comment

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Comment)

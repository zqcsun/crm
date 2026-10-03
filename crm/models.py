from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Lead(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
    
class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='manager_user')
    number = models.CharField(max_length=30)
    lead = models.ForeignKey(Lead,on_delete=models.CASCADE, related_name='lead_uder')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
    
class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='admin_user')
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE,related_name='manager_admin')

    def __str__(self):
        return self.user.get_full_name()
    
class StorageModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    product = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE, related_name = 'manager_storage')

    def __str__(self):
        return self.title
    
class PostModel(models.Model):
    storage= models.ForeignKey(StorageModel, on_delete=models.CASCADE, related_name='storage_post')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crm_posts')
    content = models.TextField()
    image= models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

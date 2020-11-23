from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.


class Post(models.Model):
    image = CloudinaryField('image',null=True,blank=True)
    # image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})



class Username(models.Model):
    title = models.CharField(max_length =30)
    image = CloudinaryField('image',null=True,blank=True)
    # image = models.ImageField(max_length =60,upload_to='images/')
    description = models.TextField(max_length =200)



    def save_username(self):
        self.save()

    def delete_username(self):
        self.delete()

    def update_username(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        photo = cls.objects.filter(title__icontains=search_term)
        return photo


    def __str__(self):
        return self.title
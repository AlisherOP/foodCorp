from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
# to mig
# to edite  the list you should first:(Item.objects.all() for checking the insides)
#1python manage.py shell then from food.models import Item. To creat objects

class Item(models.Model):

    def __str__(self):
        return self.item_name 
    user_name= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=200)
    item_price = models.IntegerField(null=True, blank=True)
    item_cal = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="items")
    item_image = models.CharField(max_length=500 , default="https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg")
    favourites= models.ManyToManyField(
        User, related_name='favorite', default=None, blank=None
    )
    #once a new item is created we should go straight to the desciption
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk}) 
    
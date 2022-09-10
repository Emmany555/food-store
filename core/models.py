from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  profileimg = models.ImageField(upload_to='profile_images', default='profile-pic.jpeg', )
  location = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.user.username


class Product(models.Model):
  name = models.CharField(max_length=200)
  # product_id = models.IntegerField()
  stock = models.IntegerField()
  price = models.FloatField(max_length=20)
  description = models.CharField(max_length=10000)
  img_url = models.CharField(max_length=2300)
  discount = models.FloatField(default=0)
  seller_contact= models.CharField(max_length=25 )

  def __str__(self):
    return self.name
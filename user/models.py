from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

    
class Profile(models.Model):
  name = models.CharField(max_length = 200,null = True,blank = True)
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  email = models.EmailField(null = True,blank = True)
  gender = models.CharField(max_length = 200,null = True,blank = True)
  paid_time = models.DateField(null=True, blank=True)
  paid = models.CharField(max_length = 200,default = "False")
  last_login = models.DateTimeField(default=datetime.now(),null = True,blank = True)
  image_url = models.ImageField(_("Image"),upload_to = upload_to,default = "images/default.png")

  def __str__(self):
    return self.name

# Create your models here.

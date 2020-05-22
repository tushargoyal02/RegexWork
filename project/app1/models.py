from django.db import models
#from phone_field import PhoneField


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    Aphone = models.CharField(max_length=12)
    # phone = PhoneField(null=False, blank=False, unique=True)
    # Aphone = PhoneField(null=False, blank=False)
    College_name = models.CharField(max_length=500) 


    def __str__(self):
        return str(self.email)

class Image(models.Model):
    model_name = models.CharField(max_length=50)
    model_pic = models.ImageField(upload_to='images/')

    def get_image(self):
        if self.model_pic and hasattr(self.model_pic, 'url'):
            return self.model_pic.url
        else:
            return '/path/to/default/image'


def __unicode__(self):
    return self.model_pic
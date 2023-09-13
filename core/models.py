from django.db import models
from django.contrib.auth.models import User


from sinrato.utils.base import basemodel
from django.db import models


# Create your models here.


 
class Contactinfo(basemodel):
    name = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Message = models.TextField(verbose_name='your user description')
    Phone = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')
    Email = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Subject = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')



    class Meta:
        verbose_name='corepost' 
        verbose_name_plural='All contact fomrs'

    def __str__(self):
        return self.name






class corep(basemodel):
   

    title=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    description=models.TextField(verbose_name='your user description')
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="core img")
    img2 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="core img")
    title2=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title3=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title4=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')



    class Meta:
        verbose_name='corepost' 
        verbose_name_plural='All product models name'

    def __str__(self):
        return self.title
    

  




class Subscriber(basemodel):
    email = models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def _str_(self):
        return self.email


    
from django.db import models

from sinrato.utils.base import basemodel


# Create your models here.


 
class Contactinfo(basemodel):
    name = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Message = models.TextField(verbose_name='your user description')
    Phone = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')
    Email = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Subject = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')





class corep(basemodel):
   

    title=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    description=models.TextField(verbose_name='your user description')
    fullname= models.CharField(max_length=20,verbose_name='Your name(Author)',help_text='max 20 character ')
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="core img")
    img2 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="core img")
    title2=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title3=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title4=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')


    class Meta:
        verbose_name='corepost' 
        verbose_name_plural='All Movie Posts'

    def __str__(self):
        return self.title
    



class FeaturedProduct(basemodel):
   

    title=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="core img")
    title2=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title3=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')
    title4=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255')

  

    class Meta:
        verbose_name='Featured' 
        verbose_name_plural='All Featured Posts'

    def __str__(self):
        return self.title
    
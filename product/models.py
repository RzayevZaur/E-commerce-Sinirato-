from django.db import models
from sinrato.utils.base import basemodel



# Create your models here.
class Manufacturer(basemodel):
    name = models.CharField(verbose_name="Manufacturer name")
    def __str__(self):
        return self.name

class Category(basemodel):
    name = models.CharField(verbose_name="category name")
    def __str__(self):
        return self.name


class shoppagemodel(basemodel):
    is_new=models.CharField(max_length=255,verbose_name='new',help_text='max character limit 255')
    title = models.CharField( max_length=255,verbose_name="Title of the your shop",help_text="max character limit 255")
    description = models.TextField(verbose_name="your user description")
    is_adviced = models.BooleanField(default=True, verbose_name="do you like  this blog")
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    img2 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    the_price=models.CharField(max_length=255,verbose_name='mehsulun qiyməti',help_text='max character limit 255')
    sale=models.CharField(max_length=255,verbose_name='mehsulun endirimli qiyməti',help_text='max character limit 255')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shoping_categroy", null=True, blank=True)
    Manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="shoping_Manufacturer",null=True,blank=True)

    class Meta:
            verbose_name = "şhopcard"
            verbose_name_plural = "All şhop Posts"

    def __str__(self):
        return self.title
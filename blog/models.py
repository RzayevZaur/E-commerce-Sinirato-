from django.db import models
from sinrato.utils.base import basemodel


# Create your models here.



class Tags(basemodel):
    title = models.CharField(verbose_name="category name")

class Category(basemodel):
    name = models.CharField(verbose_name="category name")
    
class blogp(basemodel):
    title = models.CharField( max_length=255,verbose_name="Title of the your blog",help_text="max character limit 255")
    description = models.TextField(max_length=10000, verbose_name="your user description")
    is_adviced = models.BooleanField(default=True, verbose_name="do you like  this blog")
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    img2 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    img3 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blog_category")
    tags = models.ManyToManyField(Tags, verbose_name='Taglar:', related_name="blog_tags")
    

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "All Blog Posts"

    def __str__(self):
       return self.title

class comment(basemodel):
    name = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    commet = models.TextField(verbose_name='your user description')
    Website = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')
    email = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    blog= models.ForeignKey(blogp,on_delete=models.CASCADE,related_name='blog_commet', null=True, blank=True)
 

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "All Comment Posts"

    def __str__(self):
       return self.name
    

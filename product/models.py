from django.db import models

from django.utils.text import slugify
from sinrato.utils.base import basemodel
from django.db import models










class FeaturedProduct(basemodel):
     title = models.CharField( max_length=255,verbose_name="Featured Product name",help_text="max character limit 255")
     img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")

     @property
     def product_count(self):
         return self.Featured_Product.count()
     
     class Meta:
         verbose_name='secilmis mehsul'
         verbose_name_plural='secilmis mehsullaR'
         


class Image(basemodel):
    image = models.ImageField(upload_to="product_images")


class Tags(basemodel):
    tags_name=models.CharField(verbose_name="details_tags")

    def __str__(self):
        return self.tags_name
     

class color(basemodel):
     name =models.CharField(verbose_name="color name")
     slug = models.CharField(null=True,blank=True,unique=True,db_index=True,editable=True)

     def __str__(self):
        return self.name
     
    
     def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)





class Category_color(basemodel):
     name =models.CharField(verbose_name="Category_color name")
     slug = models.CharField(null=True,blank=True,unique=True,db_index=True,editable=True)

     def __str__(self):
        return self.name
     
    
     def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(basemodel):
    name = models.CharField(verbose_name="category name")
    slug = models.CharField(null=False, blank=True,unique=True,db_index=True,editable=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Manufacturer(basemodel):
    name = models.CharField(verbose_name="Manufacturer name")
    slug = models.CharField(null=False,blank=True,unique=True,db_index=True,editable=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    


class shoppagemodel(basemodel):
    is_new=models.CharField(max_length=255,verbose_name='new',help_text='max character limit 255')
    title = models.CharField( max_length=255,verbose_name="Title of the your shop",help_text="max character limit 255")
    description = models.TextField(verbose_name="your user description")
    is_adviced = models.BooleanField(default=True, verbose_name="do you like  this blog")
    img = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    img2 = models.ImageField(upload_to= 'img/product', null=True, blank = True,  verbose_name="blog img")
    the_price=models.CharField(max_length=255,verbose_name='mehsulun qiyməti',help_text='max character limit 255')
    Ex_Tax=models.CharField(max_length=255,verbose_name='ex tax',help_text='max character limit 255')
    Brands = models.CharField(max_length=255,verbose_name='Brands',help_text='max character limit 255')
    Product_Code = models.CharField(max_length=255,verbose_name='Product Code ',help_text='max character limit 255')
    Reward_Points=  models.CharField(max_length=255,verbose_name=' Reward Points ',help_text='max character limit 255')
    Availability= models.CharField(max_length=255,verbose_name='Availability',help_text='max character limit 255')
    sale=models.CharField(max_length=255,verbose_name='mehsulun endirimli qiyməti',help_text='max character limit 255')
    detail_description=models.TextField(verbose_name="details description")
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shoping_categroy", null=True, blank=True)
    Manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE, related_name="shoping_Manufacturer",null=True,blank=True)
    tags=models.ManyToManyField(Tags,verbose_name='Taglar:', related_name="details_tags")
    category_color=models.ManyToManyField(Category_color)
    featured_Product=models.ForeignKey(FeaturedProduct,on_delete=models.CASCADE,related_name='Featured_Product',null=True,blank=True)
    slug = models.CharField(null=False, blank=True,unique=True,db_index=True,editable=True)

   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
            verbose_name = "şhopcard"
            verbose_name_plural = "All şhop Posts"

    def __str__(self):
        return self.title
     
class Review(models.Model):
    Rates = {
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "****")
    }
    Rating_review = models.IntegerField(choices=Rates, null=True, blank=True)
    user=models.CharField(verbose_name="user", max_length=150)
    review=models.CharField(verbose_name="review",max_length=150)
    date = models.DateField(auto_now_add=True)
    reviews= models.ForeignKey(shoppagemodel,on_delete=models.CASCADE,related_name='blog_commet', null=True, blank=True)
    
    class Meta:
            verbose_name = "review"
            verbose_name_plural = "All review Posts"

    def __str__(self):
         return self.user
    




class Product_version(models.Model):
   
    product = models.ForeignKey(shoppagemodel, on_delete=models.CASCADE, related_name="producwt_version", null=True, blank=True)
    details_color = models.ForeignKey(color, on_delete=models.CASCADE, related_name="product_color", null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.product.title}'s {self.details_color.name} version"
    
    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"







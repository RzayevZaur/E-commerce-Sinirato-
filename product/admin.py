from django.contrib import admin
from .models import shoppagemodel,Category,Manufacturer,color,Review,Tags,Product_version,Image,Category_color, FeaturedProduct

admin.site.register(shoppagemodel)

admin.site.register(Category)

admin.site.register(Manufacturer)


admin.site.register(color)

admin.site.register(Review)



admin.site.register(Tags)

admin.site.register(Product_version)

admin.site.register(Image)


admin.site.register(Category_color)
admin.site.register(FeaturedProduct)




# Register your models here.

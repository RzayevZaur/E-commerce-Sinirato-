from django.contrib import admin
from .models import blogp,Category, comment,Tags


admin.site.site_header= 'Sinrato project'
admin.site.site_title='Project'


@admin.register(blogp)
class BlogpAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'update']


admin.site.register(Category)
admin.site.register(comment)
admin.site.register(Tags)


# Register your models here.
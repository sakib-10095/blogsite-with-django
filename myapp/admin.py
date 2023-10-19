from django.contrib import admin

from myapp.models import Post


# Register your models here.
admin.site.register(Post)


class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','Title','Descriptions']
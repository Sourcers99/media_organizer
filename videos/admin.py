from django.contrib import admin
from .models import Star, Staralias, Channel, Subsite, Tag, Category, Video
# Register your models here.
admin.site.register(Star)
admin.site.register(Staralias)
admin.site.register(Channel)
admin.site.register(Subsite)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Video)
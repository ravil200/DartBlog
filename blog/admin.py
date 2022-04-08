from django.contrib import admin
from .models import Post, Cotegory, Tag
# Register your models here.
admin.site.register(Post)
admin.site.register(Cotegory)
admin.site.register(Tag)
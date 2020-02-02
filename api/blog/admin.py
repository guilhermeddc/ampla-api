from django.contrib import admin
from .models import BlogComments, Posts

# Register your models here.


admin.site.register(Posts)
admin.site.register(BlogComments)

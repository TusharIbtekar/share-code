from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

#admin.site.register(Post)

class PostAdmin(SummernoteModelAdmin):
  summernote_fields = '__all__'

# class PostAdmin(SummernoteModelAdmin):
#   summernote_fields = ('content', )

admin.site.register(Post, PostAdmin)
# admin.site.register(Post, PostAdmin)
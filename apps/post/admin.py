from django.contrib.admin import *
from .models import *

#admin   54321


#post
@register(ModelsPost)
class PostAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
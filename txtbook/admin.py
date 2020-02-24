from django.contrib import admin
from .models import TextbookPost
from .models import Textbook
# Register your models here.
admin.site.register(TextbookPost)

class textbook_admin(admin.ModelAdmin):
    list_display = ('title','author','dept','classnum','sect')


admin.site.register(Textbook,textbook_admin)

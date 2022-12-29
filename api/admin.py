from django.contrib import admin
from api import models

# Register your models here.

class Member_infoAdmin(admin.ModelAdmin):
    list_display = ('room', 'bed', 'member_class', 'student_ID', 'name')

admin.site.register(models.Member_info, Member_infoAdmin)
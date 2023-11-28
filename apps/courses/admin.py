from django.contrib import admin
from .models import Subject, Course, Module, Text , Image, File,  Video, Content


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner' , 'subject', 'created_at', 'updated_at')
    list_filter = list_display

class moduleadmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at', 'updated_at')
    list_filter = list_display


admin.site.register(Subject)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, moduleadmin)

admin.site.register(Image)
admin.site.register(Text)
admin.site.register(File)
admin.site.register(Video)
admin.site.register(Content)

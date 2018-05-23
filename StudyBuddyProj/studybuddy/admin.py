from django.contrib import admin

# Register your models here.
from .models import Student, StudyGroup, ChatMessage

admin.site.register(Student)
admin.site.register(StudyGroup)
admin.site.register(ChatMessage)
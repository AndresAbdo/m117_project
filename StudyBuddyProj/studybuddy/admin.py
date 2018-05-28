from django.contrib import admin

# Register your models here.
from .models import Student, StudyGroup, ChatMessage

admin.site.register(Student)
admin.site.register(StudyGroup)

class ChatMessageAdmin(admin.ModelAdmin):
	readonly_fields = ('timestamp',)

admin.site.register(ChatMessage, ChatMessageAdmin)


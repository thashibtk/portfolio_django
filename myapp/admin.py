from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'duration', 'team_size', 'created_at')
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)} # Auto-fill slug from title
    inlines = [ProjectImageInline] # Add the inline here

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'order', 'uploaded_at')
    list_filter = ('project',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'year')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'company', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject')
    list_filter = ('subject', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'message')
    ordering = ('-created_at',)
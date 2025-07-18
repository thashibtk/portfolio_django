from django.db import models
from django.db import models
from django.utils.text import slugify
import os
from django.urls import reverse


# Create your models here.

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id} - {self.file.name}"


class Project(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the project.")
    main_image = models.ImageField(
        upload_to='projects/main_images/',
        help_text="The main display image for the project."
    )
    short_description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="A brief description of the project (max 255 characters)."
    )
    description = models.TextField(help_text="A detailed description of the project.")
    tech_stack = models.CharField(
        max_length=255,
        help_text="Comma-separated list of technologies used (e.g., Django, React, MySQL)."
    )
    duration = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Duration of the project (e.g., '2 months', '6 weeks')."
    )
    team_size = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of developers in the team."
    )
    github_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="URL to the GitHub repository."
    )
    live_demo_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="URL to the live demo of the project."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, blank=True, max_length=255)

    learned = models.TextField(blank=True, null=True, help_text="what learned")


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
  
            original_slug = self.slug
            count = 1
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.main_image:
            if os.path.isfile(self.main_image.path):
                os.remove(self.main_image.path)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_details', args=[self.slug])


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='gallery_images',
        on_delete=models.CASCADE,
        help_text="The project this image belongs to."
    )
    image = models.ImageField(
        upload_to='projects/gallery_images/',
        help_text="An image for the project gallery."
    )
    caption = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional caption for the image."
    )
    order = models.IntegerField(
        default=0,
        help_text="Order in which images should appear in the gallery."
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Gallery Image"
        verbose_name_plural = "Project Gallery Images"
        ordering = ['order', 'uploaded_at']

    def __str__(self):
        return f"Image for {self.project.title} ({self.caption or self.image.name})"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def formatted_date_range(self):
        start = self.start_date.strftime("%Y %b").upper()
        end = self.end_date.strftime("%Y %b").upper() if self.end_date else "PRESENT"
        return f"{start} - {end}"
    
class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('web-development', 'Web Development'),
        ('collaboration', 'Project Collaboration'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
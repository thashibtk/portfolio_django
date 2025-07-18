# Generated by Django 5.2.1 on 2025-07-03 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the project.', max_length=200)),
                ('main_image', models.ImageField(help_text='The main display image for the project.', upload_to='projects/main_images/')),
                ('description', models.TextField(help_text='A detailed description of the project.')),
                ('tech_stack', models.CharField(help_text='Comma-separated list of technologies used (e.g., Django, React, MySQL).', max_length=255)),
                ('duration', models.CharField(blank=True, help_text="Duration of the project (e.g., '2 months', '6 weeks').", max_length=50, null=True)),
                ('team_size', models.IntegerField(blank=True, help_text='Number of developers in the team.', null=True)),
                ('github_link', models.URLField(blank=True, help_text='URL to the GitHub repository.', null=True)),
                ('live_demo_link', models.URLField(blank=True, help_text='URL to the live demo of the project.', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='An image for the project gallery.', upload_to='projects/gallery_images/')),
                ('caption', models.CharField(blank=True, help_text='Optional caption for the image.', max_length=255, null=True)),
                ('order', models.IntegerField(default=0, help_text='Order in which images should appear in the gallery.')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(help_text='The project this image belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='myapp.project')),
            ],
            options={
                'verbose_name': 'Project Gallery Image',
                'verbose_name_plural': 'Project Gallery Images',
                'ordering': ['order', 'uploaded_at'],
            },
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-11 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_course_slug_alter_subject_slug_video_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'model__in': ('Text', 'image', 'file', 'video')}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL),
        ),
    ]

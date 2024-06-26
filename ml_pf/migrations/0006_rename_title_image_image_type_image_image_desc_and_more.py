# Generated by Django 5.0.6 on 2024-06-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_pf', '0005_rename_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='image_type',
        ),
        migrations.AddField(
            model_name='image',
            name='image_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_delete_posttitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Title',
            field=models.CharField(max_length=50),
        ),
    ]

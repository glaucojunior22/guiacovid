# Generated by Django 3.0.4 on 2020-04-01 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20200331_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='source',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='source',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='source',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='source',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_by',
        ),
    ]

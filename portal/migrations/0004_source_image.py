# Generated by Django 3.0.4 on 2020-04-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20200401_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads', verbose_name='imagem'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0010_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
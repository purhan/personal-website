# Generated by Django 3.0.6 on 2020-05-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foliopage', '0018_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='link',
            field=models.URLField(default='test'),
            preserve_default=False,
        ),
    ]

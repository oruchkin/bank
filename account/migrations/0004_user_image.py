# Generated by Django 3.1.2 on 2021-09-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(default='https://www.bootdey.com/img/Content/avatar/avatar7.png', max_length=1500),
        ),
    ]

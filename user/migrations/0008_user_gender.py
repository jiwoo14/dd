# Generated by Django 2.2.4 on 2019-08-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', '남성'), ('f', '여성')], max_length=1, null=True),
        ),
    ]

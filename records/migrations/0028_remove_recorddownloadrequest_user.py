# Generated by Django 4.0.5 on 2022-06-10 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0027_recorddownloadrequest_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recorddownloadrequest',
            name='user',
        ),
    ]

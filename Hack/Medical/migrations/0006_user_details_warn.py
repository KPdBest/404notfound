# Generated by Django 2.0 on 2019-10-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medical', '0005_auto_20191014_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='warn',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.0.2 on 2018-03-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterWeiBo', '0018_auto_20180328_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='packageName',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='science',
            name='url',
            field=models.FileField(upload_to='public/'),
        ),
    ]

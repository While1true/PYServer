# Generated by Django 2.0.2 on 2018-03-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterWeiBo', '0004_auto_20180307_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordCloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artical_id', models.IntegerField()),
                ('user', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]

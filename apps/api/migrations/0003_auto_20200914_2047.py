# Generated by Django 3.1.1 on 2020-09-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bid_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='event',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='sport',
            field=models.IntegerField(null=True),
        ),
    ]

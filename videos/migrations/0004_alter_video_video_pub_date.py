# Generated by Django 4.0.3 on 2022-04-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_channel_channel_subsite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_pub_date',
            field=models.DateField(blank=True, null=True, verbose_name='Video Published'),
        ),
    ]

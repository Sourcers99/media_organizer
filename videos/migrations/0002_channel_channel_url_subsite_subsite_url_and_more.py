# Generated by Django 4.0.3 on 2022-04-10 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel_url',
            field=models.URLField(default=None, verbose_name='Channel URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subsite',
            name='subsite_url',
            field=models.URLField(default=None, verbose_name='Subsite URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_desc',
            field=models.TextField(default=None, verbose_name='Video Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(default=None, verbose_name='Video URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Channel Image'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_name',
            field=models.CharField(max_length=50, verbose_name='Channel Name'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_subsite',
            field=models.ManyToManyField(to='videos.subsite', verbose_name='Subsite'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_alias',
            field=models.ManyToManyField(to='videos.staralias', verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_bio',
            field=models.TextField(verbose_name='Star Bio'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_boob_size',
            field=models.CharField(max_length=50, verbose_name='Star Boob Size'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_dob',
            field=models.CharField(max_length=50, verbose_name='Star DOB'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Trans', 'Trans')], default='Female', max_length=50, verbose_name='Star Gender'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Star Image'),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_name',
            field=models.CharField(max_length=50, verbose_name='Star Name'),
        ),
        migrations.AlterField(
            model_name='subsite',
            name='subsite_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Subsite Image'),
        ),
        migrations.AlterField(
            model_name='subsite',
            name='subsite_name',
            field=models.CharField(max_length=50, verbose_name='Subsite Name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Tag Image'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50, verbose_name='Tag Name'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_category',
            field=models.ManyToManyField(to='videos.category', verbose_name='Video Category'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.channel', verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_image',
            field=models.ImageField(upload_to='./media/images/', verbose_name='Video Image'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_name',
            field=models.CharField(max_length=50, verbose_name='Video Name'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_path',
            field=models.CharField(max_length=50, verbose_name='Video Path'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_pub_date',
            field=models.DateField(verbose_name='Video Published'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_stars',
            field=models.ManyToManyField(to='videos.star', verbose_name='Stars'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_tags',
            field=models.ManyToManyField(to='videos.tag', verbose_name='Video Tag'),
        ),
    ]

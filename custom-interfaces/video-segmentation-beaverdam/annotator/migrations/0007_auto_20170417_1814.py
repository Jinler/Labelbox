# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0006_video_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(blank=True, help_text='6 digit hex.', max_length=6),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(blank=True, help_text='Name of class label option.', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='annotation',
            field=models.TextField(blank=True, help_text='A JSON blob containing all user annotation sent from client.'),
        ),
        migrations.AlterField(
            model_name='video',
            name='filename',
            field=models.CharField(blank=True, help_text='Name of the video file.The video should be publically accessible by at <host><filename>.', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='host',
            field=models.CharField(blank=True, help_text='Path to prepend to filenames to form the url for this video or the images in `image_list`.', max_length=1048),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_list',
            field=models.TextField(blank=True, help_text='List of filenames of images to be used as video frames, in JSON format.When present, image list is assumed and <filename> is ignored.'),
        ),
        migrations.AlterField(
            model_name='video',
            name='rejected',
            field=models.BooleanField(default=False, help_text='Rejected by expert.'),
        ),
        migrations.AlterField(
            model_name='video',
            name='source',
            field=models.CharField(blank=True, help_text='Name of video source or type, for easier grouping/searching of videos.This field is not used by BeaverDam and only facilitates querying on videos by type.', max_length=1048),
        ),
        migrations.AlterField(
            model_name='video',
            name='verified',
            field=models.BooleanField(default=False, help_text='Verified as correct by expert.'),
        ),
    ]
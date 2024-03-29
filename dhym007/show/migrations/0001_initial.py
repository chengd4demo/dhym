# Generated by Django 2.1.7 on 2019-11-21 15:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dhym_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_name', models.CharField(max_length=16)),
                ('message_phone', models.CharField(max_length=32)),
                ('message_content', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'dhym_message',
            },
        ),
        migrations.CreateModel(
            name='dhym_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(max_length=128, upload_to='news')),
                ('news_title', models.CharField(max_length=64)),
                ('news_user', models.CharField(max_length=32)),
                ('news_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('news_count', models.BigIntegerField(max_length=11)),
                ('news_paper', models.CharField(max_length=255)),
                ('news_content', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'dhym_news',
            },
        ),
        migrations.CreateModel(
            name='dhym_root',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_user', models.CharField(max_length=32)),
                ('root_pwd', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'dhym_root',
            },
        ),
    ]

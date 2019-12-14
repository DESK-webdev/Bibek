# Generated by Django 2.2.1 on 2019-12-14 06:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_blogstory_festival_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Bio', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='author-images')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogstory',
            name='datetime',
        ),
        migrations.AddField(
            model_name='blogstory',
            name='slug',
            field=models.SlugField(default='', help_text='It will auto-complete automically!', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='blogstory',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='festival',
            name='slug',
            field=models.SlugField(default='', help_text='It will auto-complete automically!', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='', help_text='It will auto-complete automically!', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='todolist',
            name='slug',
            field=models.SlugField(default='', help_text='It will auto-complete automically!', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='blogstory',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='festival',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='blogstory',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tourism.Author'),
        ),
    ]

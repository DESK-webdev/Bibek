# Generated by Django 2.2.3 on 2019-11-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_auto_20191124_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Blogimages')),
                ('body', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='festiveimages')),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ToDolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='ToDoimages')),
                ('description', models.TextField()),
            ],
        ),
    ]
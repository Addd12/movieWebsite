# Generated by Django 3.1.7 on 2021-04-04 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('cast', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/thumbnail')),
                ('year', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.CharField(max_length=100)),
                ('age_restriction', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
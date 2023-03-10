# Generated by Django 4.1.5 on 2023-01-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('speaker_name', models.CharField(max_length=40)),
                ('speakers_avatar', models.ImageField(upload_to='app/images')),
                ('date_select', models.DateField()),
                ('duration', models.DurationField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'ordering': ['speaker_name', 'date_select', 'duration'],
            },
        ),
    ]

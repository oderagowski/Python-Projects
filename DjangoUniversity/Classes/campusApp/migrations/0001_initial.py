# Generated by Django 4.1.6 on 2023-02-13 19:10

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=70)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]

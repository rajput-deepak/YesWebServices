# Generated by Django 4.1.2 on 2022-10-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=12)),
                ('msg', models.CharField(max_length=150)),
            ],
        ),
    ]
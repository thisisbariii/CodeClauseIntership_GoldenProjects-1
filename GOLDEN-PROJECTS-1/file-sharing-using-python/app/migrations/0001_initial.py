# Generated by Django 4.2.6 on 2023-10-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myfile',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='myfile')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

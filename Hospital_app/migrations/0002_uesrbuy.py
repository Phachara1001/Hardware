# Generated by Django 4.2.7 on 2024-01-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uesrbuy',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('tal', models.CharField(max_length=255)),
            ],
        ),
    ]
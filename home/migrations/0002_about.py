# Generated by Django 4.2.3 on 2023-08-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=64)),
                ('parag1', models.TextField()),
                ('parag2', models.TextField()),
            ],
        ),
    ]
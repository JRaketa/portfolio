# Generated by Django 2.2.17 on 2021-02-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.TextField(max_length=500)),
                ('year', models.DateField(max_length=10)),
                ('journal', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=300)),
            ],
        ),
    ]

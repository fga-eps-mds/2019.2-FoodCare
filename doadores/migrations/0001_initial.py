# Generated by Django 2.2.2 on 2019-10-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('cpnj', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
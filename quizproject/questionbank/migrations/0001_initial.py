# Generated by Django 3.2 on 2021-06-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qbank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qus', models.CharField(max_length=150)),
                ('op1', models.CharField(max_length=150)),
                ('op2', models.CharField(max_length=150)),
                ('op3', models.CharField(max_length=150)),
                ('op4', models.CharField(max_length=150)),
                ('ans', models.CharField(max_length=150)),
            ],
        ),
    ]

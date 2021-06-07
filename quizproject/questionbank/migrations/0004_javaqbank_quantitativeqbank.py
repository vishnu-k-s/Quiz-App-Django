# Generated by Django 3.2 on 2021-06-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbank', '0003_rename_djangoqank_djangoqbank'),
    ]

    operations = [
        migrations.CreateModel(
            name='JavaQBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('option1', models.CharField(max_length=150)),
                ('option2', models.CharField(max_length=150)),
                ('option3', models.CharField(max_length=150)),
                ('option4', models.CharField(max_length=150)),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeQBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('option1', models.CharField(max_length=150)),
                ('option2', models.CharField(max_length=150)),
                ('option3', models.CharField(max_length=150)),
                ('option4', models.CharField(max_length=150)),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to=None)),
                ('others', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waterings', to='plants.Plant')),
            ],
        ),
    ]

# Generated by Django 4.2.11 on 2024-05-06 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GPT_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a2', models.CharField(max_length=1000)),
                ('q2', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Answers2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a2', models.CharField(max_length=1000)),
                ('q2', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='q2',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
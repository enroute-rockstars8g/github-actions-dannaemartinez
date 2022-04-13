# Generated by Django 4.0.3 on 2022-04-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
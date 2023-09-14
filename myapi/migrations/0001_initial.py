# Generated by Django 4.2.5 on 2023-09-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('current_state', models.CharField(max_length=50)),
                ('incorrect_guesses', models.IntegerField(default=0)),
                ('max_incorrect_guesses', models.IntegerField(default=0)),
                ('status', models.CharField(default='InProgress', max_length=10)),
            ],
        ),
    ]
# Generated by Django 2.1.5 on 2019-04-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0002_mcqscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mcqscore',
            old_name='score',
            new_name='mcqscore',
        ),
    ]

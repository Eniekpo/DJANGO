# Generated by Django 4.1.7 on 2023-04-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djforms', '0006_candidate_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(max_length=18),
        ),
    ]
# Generated by Django 5.1.5 on 2025-01-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

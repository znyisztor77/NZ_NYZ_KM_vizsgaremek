# Generated by Django 4.2.6 on 2024-01-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raktar_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anyagtipus',
            name='anyagtipusa',
            field=models.CharField(choices=[('Aluminium', 'Aluminium'), ('Horganyzott', 'Horganyzott'), ('Plexi', 'Plexi'), ('Rozsdamentes', 'Rozsdamentes'), ('Szenacel', 'Szenacél')], max_length=255),
        ),
    ]

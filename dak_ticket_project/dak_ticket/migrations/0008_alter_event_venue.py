# Generated by Django 3.2.12 on 2024-03-27 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dak_ticket', '0007_rename_event_type_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='dak_ticket.venue'),
        ),
    ]

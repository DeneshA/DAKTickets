# Generated by Django 5.0.3 on 2024-03-27 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dak_ticket', '0004_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='event_type',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default=3, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dak_ticket.venue'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
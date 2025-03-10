# Generated by Django 4.2.2 on 2025-02-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_task_status_check_task_status_check'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='sprint',
            name='end_date_after_start_date',
        ),
        migrations.AddConstraint(
            model_name='sprint',
            constraint=models.CheckConstraint(check=models.Q(('end_date__gt', models.F('start_date'))), name='end_date_after_start_date'),
        ),
    ]

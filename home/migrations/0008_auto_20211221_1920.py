# Generated by Django 3.2.6 on 2021-12-21 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211217_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='delete_id',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='messages',
            name='is_read',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='course_id',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='type',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='refund',
            name='approval_status',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='spam',
            name='approval_status',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]
# Generated by Django 3.2.6 on 2021-12-21 19:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211221_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admincontrol',
            name='offer_percentage',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='admincontrol',
            name='priority',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='admincontrol',
            name='student_tax',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='admincontrol',
            name='teacher_tax',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='messages',
            name='course_id',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(11)]),
        ),
    ]

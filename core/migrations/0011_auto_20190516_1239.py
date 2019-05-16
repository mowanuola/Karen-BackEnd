# Generated by Django 2.1.7 on 2019-05-16 12:39

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190516_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=computed_property.fields.ComputedIntegerField(blank=True, compute_from='get_age', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodtype',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('ab', 'AB'), ('o', 'O')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bmi',
            field=computed_property.fields.ComputedIntegerField(blank=True, compute_from='get_bmi', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dci',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='useractivity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
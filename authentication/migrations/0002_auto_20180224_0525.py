# Generated by Django 2.0.2 on 2018-02-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='guardian_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='student_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-26 08:32

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200926_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
    ]
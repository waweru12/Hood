# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-07 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Thehood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoodDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('detailtype', models.CharField(choices=[('Contact', 'Contact'), ('Business', 'Business')], max_length=255)),
                ('contact', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.CharField(choices=[('South B', 'South B'), ('Makongeni', 'Makongeni'), ('Kileleshwa', 'Kileleshwa')], max_length=255)),
                ('pic', models.ImageField(blank=True, upload_to='hoods/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Thehood.Neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hooddetails',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Thehood.Neighbourhood'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-23 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Date', models.DateField()),
                ('Position', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Telephone', models.CharField(max_length=200, null=True)),
                ('Members', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('genre', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(choices=[('pending', 'pending'), ('confirm', 'confirm'), ('cancel', 'cancel')], default='pending', max_length=20)),
                ('Additional_details', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Handled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Select_event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.event')),
            ],
        ),
    ]

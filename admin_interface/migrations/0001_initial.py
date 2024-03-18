# Generated by Django 5.0.3 on 2024-03-18 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genere', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('runtime', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actor', models.CharField(max_length=100)),
                ('actress', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('star_cast', models.TextField()),
                ('release_date', models.DateField()),
                ('trailer_link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='admin_interface.movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='admin_interface.theater')),
            ],
        ),
    ]

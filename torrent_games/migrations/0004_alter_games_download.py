# Generated by Django 4.2.6 on 2023-11-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrent_games', '0003_games_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='download',
            field=models.FileField(null=True, upload_to='Downloads/'),
        ),
    ]

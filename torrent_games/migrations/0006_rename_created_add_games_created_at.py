# Generated by Django 4.2.6 on 2023-11-09 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torrent_games', '0005_alter_games_download'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='created_add',
            new_name='created_at',
        ),
    ]

# Generated by Django 4.1 on 2022-08-09 15:25

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('designer', models.CharField(max_length=50)),
                ('year_released', models.IntegerField()),
                ('number_of_players', models.IntegerField()),
                ('estimated_time_to_play', models.IntegerField()),
                ('age_recommendation', models.IntegerField()),
                ('game_categories', models.ManyToManyField(related_name='games', to='raterprojectapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='raterprojectapi/uploads/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player'),
        ),
    ]

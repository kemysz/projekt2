# Generated by Django 4.1.6 on 2023-02-22 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('num_apps', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.computer')),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room'),
        ),
    ]
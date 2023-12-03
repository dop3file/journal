# Generated by Django 4.2.7 on 2023-12-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anthropometric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('vital_capacity', models.IntegerField(blank=True, null=True)),
                ('strength', models.IntegerField(blank=True, null=True)),
                ('right_hand_strength', models.IntegerField(blank=True, null=True)),
                ('left_hand_strength', models.IntegerField(blank=True, null=True)),
                ('chs', models.IntegerField(blank=True, null=True)),
                ('ads', models.IntegerField(blank=True, null=True)),
                ('add', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

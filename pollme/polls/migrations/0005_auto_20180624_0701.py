# Generated by Django 2.0.5 on 2018-06-24 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180624_0656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['poll']},
        ),
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
    ]

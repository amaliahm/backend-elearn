# Generated by Django 4.0.1 on 2024-06-06 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0010_prof_assistant_responsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='responsable',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.DO_NOTHING, to='promo.responsable'),
            preserve_default=False,
        ),
    ]
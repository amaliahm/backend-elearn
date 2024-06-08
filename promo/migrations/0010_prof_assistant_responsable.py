# Generated by Django 4.0.1 on 2024-06-06 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_groups_alter_user_user_permissions'),
        ('promo', '0009_alter_etudiant_cohorte_alter_etudiant_promo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('prof_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='promo.prof')),
            ],
            options={
                'abstract': False,
            },
            bases=('promo.prof',),
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('prof_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='promo.prof')),
            ],
            options={
                'abstract': False,
            },
            bases=('promo.prof',),
        ),
    ]
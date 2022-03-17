# Generated by Django 3.2.12 on 2022-03-16 14:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payoff', '0011_fiscalyear_deletecascade'),
        ('contacts', '0004_length_field'),
        ('condominium', '0018_fiscalyear_deletecascade'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyLotCustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='tantime')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.customfield', verbose_name='field')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominium.propertylot', verbose_name='property')),
            ],
            options={
                'verbose_name': 'custom field value',
                'verbose_name_plural': 'custom field values',
                'default_permissions': [],
            },
        ),
        migrations.AddField(
            model_name='set',
            name='secondarykey',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.customfield', verbose_name='distribution key'),
        ),
    ]

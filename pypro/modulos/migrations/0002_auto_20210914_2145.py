# Generated by Django 3.2.7 on 2021-09-15 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='modulo',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modulo',
            name='publico',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_usuario_usuarioprincipal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembronuevo',
            name='email',
        ),
        migrations.AddField(
            model_name='miembronuevo',
            name='celular',
            field=models.CharField(default='No especificado', max_length=15),
        ),
    ]

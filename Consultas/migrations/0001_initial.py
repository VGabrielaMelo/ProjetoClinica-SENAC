# Generated by Django 4.1.1 on 2022-09-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('crm', models.CharField(blank=True, max_length=10, null=True)),
                ('data_nasc', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveis', models.TextField(choices=[('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediario'), ('Avançado', 'Avancado')])),
                ('categorias', models.TextField(choices=[('Hipertrofia', 'Hipertrofia'), ('Resistência', 'Resistencia'), ('Força', 'Forca')])),
            ],
        ),
        migrations.CreateModel(
            name='Exercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parte_corpo', models.TextField()),
                ('equipamento', models.TextField()),
                ('gif', models.TextField()),
                ('nome', models.TextField()),
                ('alvo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Treinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treino', models.TextField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])),
                ('grupo_muscular1', models.TextField(choices=[('Peito', 'Peito'), ('Costas', 'Costas'), ('Bíceps', 'Biceps'), ('Triceps', 'Triceps'), ('Perna', 'Perna'), ('Abdomen', 'Abdomen'), ('Nenhum', 'Nenhum')])),
                ('grupo_muscular2', models.TextField(choices=[('Peito', 'Peito'), ('Costas', 'Costas'), ('Bíceps', 'Biceps'), ('Triceps', 'Triceps'), ('Perna', 'Perna'), ('Abdomen', 'Abdomen'), ('Nenhum', 'Nenhum')])),
                ('exercicios', models.ManyToManyField(to='home.exercicios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuario')),
            ],
        ),
    ]
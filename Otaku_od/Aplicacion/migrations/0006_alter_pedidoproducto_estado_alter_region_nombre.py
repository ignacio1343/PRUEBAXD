# Generated by Django 5.0.6 on 2024-06-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0005_pedidoproducto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoproducto',
            name='estado',
            field=models.CharField(choices=[('Cancelado', 'Cancelado'), ('En circulacion', 'En circulacion'), ('Entregado', 'Entregado'), ('Pagado', 'Pagado')], default='Pagado', max_length=50),
        ),
        migrations.AlterField(
            model_name='region',
            name='nombre',
            field=models.CharField(choices=[('II', 'Antofagasta'), ('XV', 'Arica y Parinacota'), ('III', 'Atacama'), ('XI', 'Aysén'), ('VIII', 'Biobío'), ('IV', 'Coquimbo'), ('IX', 'La Araucanía'), ('X', 'Los Lagos'), ('XIV', 'Los Ríos'), ('XII', 'Magallanes'), ('VII', 'Maule'), ('XIII', 'Metropolitana'), ('VI', "O'Higgins"), ('I', 'Tarapacá'), ('V', 'Valparaíso'), ('XVI', 'Ñuble')], default='Pagado', max_length=50),
        ),
    ]
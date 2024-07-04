# Generated by Django 4.2.1 on 2024-07-04 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'db_estado',
            },
        ),
        migrations.CreateModel(
            name='EstadoEntrega',
            fields=[
                ('id_estado_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('estado_entrega', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'db_estado_entrega',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estado')),
                ('estado_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadoentrega')),
            ],
            options={
                'db_table': 'db_factura',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=125)),
                ('direccion', models.CharField(max_length=125)),
                ('telefono', models.CharField(max_length=125)),
                ('correo', models.EmailField(max_length=254)),
                ('codigo_postal', models.IntegerField()),
            ],
            options={
                'db_table': 'db_orden',
            },
        ),
        migrations.CreateModel(
            name='ProductoFactura',
            fields=[
                ('id_producto_factura', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=125)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='app.factura')),
            ],
            options={
                'db_table': 'db_producto_factura',
            },
        ),
        migrations.CreateModel(
            name='HistorialRechazo',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factura')),
            ],
            options={
                'db_table': 'db_historial',
            },
        ),
        migrations.AddField(
            model_name='factura',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.orden'),
        ),
        migrations.CreateModel(
            name='Aceptacion',
            fields=[
                ('id_aceptacion', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(null=True, upload_to='aceptacion')),
                ('direccionAcept', models.CharField(max_length=500)),
                ('rutAcept', models.CharField(max_length=500)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factura')),
            ],
            options={
                'db_table': 'db_aceptacion',
            },
        ),
    ]

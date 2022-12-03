# Generated by Django 4.1.3 on 2022-12-03 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.IntegerField(max_length=30)),
                ('fecha_creacion', models.DateField(max_length=30)),
                ('fecha_vencimiento', models.DateField(max_length=30)),
                ('precio_venta', models.IntegerField(max_length=30)),
                ('precio_costo', models.IntegerField(max_length=30)),
                ('estado', models.CharField(choices=[('Bien', 'Poco'), ('Mal', 'Mal'), ('Critico', 'Critico')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroClienteTienda',
            fields=[
                ('id_cli', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(choices=[('Targeta', 'Targeta'), ('Efectivo', 'Efectivo')], max_length=15)),
                ('dni', models.IntegerField(max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('distrito', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tiendas',
            fields=[
                ('id_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tienda', models.CharField(max_length=45)),
                ('nombre_dueño', models.CharField(max_length=45)),
                ('fecha_alquiler', models.DateField()),
                ('categoria', models.CharField(choices=[('Juegos', 'Juegos'), ('Comida', 'Comida'), ('Ropa', 'Ropa')], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=40)),
                ('celular', models.IntegerField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('monto_total', models.FloatField()),
                ('nombres_cli', models.CharField(max_length=45)),
                ('dni_cli', models.IntegerField(max_length=8)),
                ('tipo_pago', models.CharField(max_length=15)),
                ('numero_boleta', models.CharField(max_length=15)),
                ('fecha_pago', models.DateField()),
                ('ruc', models.IntegerField(max_length=20)),
                ('igb', models.IntegerField()),
                ('nombres', models.CharField(max_length=45)),
                ('id_cli', models.ForeignKey(db_column='id_cli', on_delete=django.db.models.deletion.DO_NOTHING, to='core.registroclientetienda')),
                ('nombre_producto', models.ForeignKey(db_column='nombre', on_delete=django.db.models.deletion.DO_NOTHING, to='core.productos')),
                ('nombre_tienda', models.ForeignKey(db_column='nombre_tienda', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tiendas')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(choices=[('administrador general', 'administrador general'), ('administrador nivel1', 'administrador nivel1'), ('administrador nivel2', 'administrador nivel2')], max_length=45)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.usuarios')),
            ],
        ),
    ]

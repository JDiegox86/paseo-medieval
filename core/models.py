from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuarios(models.Model):
    FEMENINO = 'Femenino'
    MASCULINO = 'Masculino'

    GENERO_CHOICES = [
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino'),
    ]
    dni = models.IntegerField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    celular = models.IntegerField(max_length=9)
    direccion = models.CharField(max_length=50)
    distrito = models.CharField(max_length=30)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'usuarios'
        db_table = 'usuarios'


class Roles(models.Model):
    ADMINISTRADOR_GENERAL = 'administrador general'
    ADMINISTRADOR_NIVEL1 = 'administrador nivel1'
    ADMINISTRADOR_NIVEL2 = 'administrador nivel2'

    CARGOS_CHOICES = [
        (ADMINISTRADOR_GENERAL, 'administrador general'),
        (ADMINISTRADOR_NIVEL1, 'administrador nivel1'),
        (ADMINISTRADOR_NIVEL2, 'administrador nivel2'),
    ]
    id_rol = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=45, choices=CARGOS_CHOICES)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return self.id_rol

    class Meta:
        verbose_name = 'roles'
        db_table = 'roles'


class Productos(models.Model):
    BIEN = 'Bien'
    MAL = 'Mal'
    CRITICO = 'Critico'

    ESTADO_CHOICES = [
        (BIEN, 'Poco'),
        (MAL, 'Mal'),
        (CRITICO, 'Critico'),
    ]
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField(max_length=30)
    fecha_creacion = models.DateField(max_length=30)
    fecha_vencimiento = models.DateField(max_length=30)
    precio_venta = models.IntegerField(max_length=30)
    precio_costo = models.IntegerField(max_length=30)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.id_producto

    class Meta:
        verbose_name = 'productos'
        db_table = 'productos'


class RegistroClienteTienda(models.Model):
    TARGETA = 'Targeta'
    EFECTIVO = 'Efectivo'

    TIPO_PAGO_CHOICES = [
        (TARGETA, 'Targeta'),
        (EFECTIVO, 'Efectivo'),
    ]
    id_cli = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=15, choices=TIPO_PAGO_CHOICES)
    dni = models.IntegerField(max_length=8)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)

    def __str__(self):
        return self.id_cli

    class Meta:
        verbose_name = 'registroclientetienda'
        db_table = 'registroclientetienda'



class Tiendas(models.Model):
    JUEGOS = 'Juegos'
    COMIDA = 'Comida'
    ROPA = 'Ropa'

    CATEGORIAS_CHOICES = [
        (JUEGOS, 'Juegos'),
        (COMIDA, 'Comida'),
        (ROPA, 'Ropa'),
    ]
    id_tienda = models.AutoField(primary_key=True)
    nombre_tienda = models.CharField(max_length=45)
    nombre_dueño = models.CharField(max_length=45)
    fecha_alquiler = models.DateField()
    categoria = models.CharField(max_length=45, choices=CATEGORIAS_CHOICES)

    def __str__(self):
        return self.id_tienda

    class Meta:
        verbose_name = 'tiendas'
        db_table = 'tiendas'


class Ventas(models.Model):
    TARGETA = 'Targeta'
    EFECTIVO = 'Efectivo'

    TIPO_PAGO_CHOICES = [
        (TARGETA, 'Targeta'),
        (EFECTIVO, 'Efectivo'),
    ]
    monto = models.FloatField()
    monto_total = models.FloatField()
    id_cli = models.ForeignKey(RegistroClienteTienda, models.DO_NOTHING, db_column='id_cli')
    nombres_cli = models.CharField(max_length=45)
    dni_cli = models.IntegerField(max_length=8)
    tipo_pago = models.CharField(max_length=15)
    numero_boleta = models.CharField(max_length=15)
    fecha_pago = models.DateField()
    ruc = models.IntegerField(max_length=20)
    igb = models.IntegerField()
    nombre_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='nombre')
    nombres = models.CharField(max_length=45)
    nombre_tienda = models.ForeignKey(Tiendas, models.DO_NOTHING, db_column='nombre_tienda')

    def __str__(self):
        return self.nombres_cli

    class Meta:
        verbose_name = 'ventas'
        db_table = 'ventas'
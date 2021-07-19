from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=150, blank=False, null=False, unique=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.marca}'

    class Meta:
        db_table = 'brands'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=150, blank=False, null=False, unique=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.tipo}'

    class Meta:
        db_table = 'types'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']



class Transmision(models.Model):
    id = models.AutoField(primary_key=True)
    transmision = models.CharField(max_length=50, blank=False, null=False, unique=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.transmision}'

    class Meta:
        db_table = 'transmission'
        verbose_name = 'Transmision'
        ordering = ['id']


class Auto(models.Model):

    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=150, blank=False, null=False)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    version = models.CharField(max_length=200)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    costo = models.FloatField()
    motor = models.CharField(max_length=100)
    potencia = models.CharField(max_length=50)
    torque = models.CharField(max_length=50)
    cilindrada = models.CharField(max_length=50)
    id_transmision = models.ForeignKey(Transmision, on_delete=models.CASCADE)
    año_fabricacion = models.IntegerField()
    largo = models.FloatField()
    ancho = models.FloatField()
    alto = models.FloatField()
    estado = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='autos', max_length=255, blank=False, null=False, default='-')
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.modelo} - {self.id_marca}'

    class Meta:
        db_table = 'cars'
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'
        ordering = ['id_marca']
    




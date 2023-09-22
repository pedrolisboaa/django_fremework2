from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, unique=True, help_text='Maximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
    
    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


class Carro(models.Model):
    """
    # OneToOneFiel
    Cada carro so pode se relacionar com um chassi
    e cada chassi so pode se relacionar com um carro

    # Foreing Key (one To many)
    Cada carro so possui uma montadora 
    Uma montadora pode possuir vários carros

    #ManyToMany
    Um carro pode ser dirigido por vários motoristas
    e um motorista pode dirigir diversos carros.
    """
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model())
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=50, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'
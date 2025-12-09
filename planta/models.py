from django.db import models

class Plant(models.Model):
    WATER_LEVELS = [
        ('muy_poca', 'Muy poca'),
        ('poca', 'Poca'),
        ('moderada', 'Moderada'),
        ('mucha', 'Mucha'),
    ]
    LIGHT_TYPES = [
        ('sombra', 'Sombra'),
        ('indirecta', 'Luz indirecta'),
        ('parcial', 'Luz parcial'),
        ('directa', 'Sol directo'),
    ]
    FERTILIZER_FREQ = [
        ('poco', 'Poco'),
        ('moderado', 'Moderado'),
        ('frecuente', 'Frecuente'),
    ]
    LOCATION = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('ambas', 'Ambas'),
    ]
    MAINTENANCE = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
    ]

    name = models.CharField(max_length=120, unique=True)
    water = models.CharField(max_length=20, choices=WATER_LEVELS)
    light = models.CharField(max_length=20, choices=LIGHT_TYPES)
    fertilizer = models.CharField(max_length=20, choices=FERTILIZER_FREQ)
    location = models.CharField(max_length=20, choices=LOCATION)
    maintenance = models.CharField(max_length=20, choices=MAINTENANCE)
    image_url = models.URLField(blank=True)  # sigue permitiendo URLs externas
    image_file = models.ImageField(upload_to='plant_images/', blank=True, null=True)  # nueva opción para subir fotos
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

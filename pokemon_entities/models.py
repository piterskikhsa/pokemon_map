from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Имя на русском', max_length=200)
    title_en = models.CharField('Имя на английском', max_length=200, blank=True)
    title_jp = models.CharField('Имя на японском', max_length=200, blank=True)
    img_url = models.ImageField('Картинка')
    description = models.TextField('Описание')
    evolution_from = models.ForeignKey('Pokemon',
                                       related_name='evolutions_from',
                                       verbose_name='Эволюционировал из',
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey('Pokemon',
                                related_name='pokemon_entities',
                                verbose_name='Покемон',
                                on_delete=models.CASCADE)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Время появления')
    disappeared_at = models.DateTimeField('Время исчезновения')
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)

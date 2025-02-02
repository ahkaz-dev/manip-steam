from django.db import models

class Game(models.Model):
    STATUS_CHOICE = [
        ('sc1', 'Passed'),
        ('sc2', 'Not finished'),
        ('sc3', 'Drop'),
        ('sc4', 'Not started'),
    ]
    GAMERATING_CHOICE = [
        ('gmc1', '1'),
        ('gmc2', '2'),
        ('gmc3', '3'),
        ('gmc4', '4'),
        ('gmc5', '5'),
    ]
    
    appid = models.CharField(max_length=30, verbose_name='Steam app id')
    name = models.CharField(max_length=255, verbose_name='Steam app name')
    playtime_forever = models.CharField(max_length=30, verbose_name='User play hours')
    status = models.CharField(max_length=55, choices=STATUS_CHOICE, verbose_name='Gameplay status', default='sc4')
    local_rating = models.CharField(max_length=10, choices=GAMERATING_CHOICE, verbose_name='Your game rating', default='1')
    local_review = models.CharField(max_length=550, verbose_name='Your local game review')
    
    def __str__(self):
        return self.name;
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        
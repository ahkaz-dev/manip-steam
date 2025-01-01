from django.db import models

class Game(models.Model):
    STATUS_CHOICE = [
        ('sc1', 'Passed'),
        ('sc2', 'Not finished'),
        ('sc3', 'Drop'),
        ('sc4', 'Not started'),
    ]
    
    appid = models.CharField(max_length=30, verbose_name='Steam app id')
    name = models.CharField(max_length=255, verbose_name='Steam app name')
    playtime_forever = models.CharField(max_length=30, verbose_name='User play hours')
    status = models.CharField(max_length=55, choices=STATUS_CHOICE, verbose_name='Gameplay status', default='Not started')
    
    def __str__(self):
        return self.get_status_display();
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        
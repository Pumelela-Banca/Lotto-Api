from django.db import models
from django.db.models import JSONField



class Daily(models.Model):
    """
    Dailly lotto model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    bonus = models.IntegerField()


class PowerBall(models.Model):
    """
    Powerball model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    powerball = models.IntegerField()


class PowerBallPlus(models.Model):
    """
    Powerball Plus model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    powerball = models.IntegerField()


class Lotto(models.Model):
    """
    Dailly lotto model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    bonus = models.IntegerField()


class Lotto1(models.Model):
    """
    Dailly lotto model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    bonus = models.IntegerField()


class Lotto2(models.Model):
    """
    Dailly lotto model
    """
    date = models.DateField()
    numbers = JSONField(default=list)
    bonus = models.IntegerField()

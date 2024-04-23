"""
Converting python pbjects to JSON objects
"""
from rest_framework import serializers
from .models import (Daily, PowerBall, PowerBallPlus, Lotto, Lotto1, Lotto2)


class DailySerializer(serializers.ModelSerializer):
    """
    Daily lotto serializer
    """
    class Meta:
        model = Daily
        fields = ['id', 'date', 'numbers', 'bonus']


class PowerBallSerializer(serializers.ModelSerializer):
    """
    Powerball serializer
    """
    class Meta:
        model = PowerBall
        fields = ['id', 'date', 'numbers', 'powerball']


class PowerBallPlusSerializer(serializers.ModelSerializer):
    """
    Powerball Plus serializer
    """
    class Meta:
        model = PowerBallPlus
        fields = ['id', 'date', 'numbers', 'powerball']


class LottoSerializer(serializers.ModelSerializer):
    """
    Lotto serializer
    """
    class Meta:
        model = Lotto
        fields = ['id', 'date', 'numbers', 'bonus']


class Lotto1Serializer(serializers.ModelSerializer):
    """
    Lotto1 serializer
    """
    class Meta:
        model = Lotto1
        fields = ['id', 'date', 'numbers', 'bonus']


class Lotto2Serializer(serializers.ModelSerializer):
    """
    Lotto2 serializer
    """
    class Meta:
        model = Lotto2
        fields = ['id', 'date', 'numbers', 'bonus']

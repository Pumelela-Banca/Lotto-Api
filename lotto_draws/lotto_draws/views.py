"""
List of views for the lotto_draws app.
"""
from django.http import JsonResponse
from rest_framework import viewsets
from models import (Daily, PowerBall, 
                    PowerBallPlus, Lotto, Lotto1, Lotto2)
from  serializers import (DailySerializer, PowerBallSerializer, 
                            PowerBallPlusSerializer, LottoSerializer, 
                            Lotto1Serializer, Lotto2Serializer)


def all_draws():
    """
    Return all the draws
    """
    daily = Daily.objects.all()
    powerball = PowerBall.objects.all()
    powerball_plus = PowerBallPlus.objects.all()
    lotto = Lotto.objects.all()
    lotto1 = Lotto1.objects.all()
    lotto2 = Lotto2.objects.all()

    return daily, powerball, powerball_plus, lotto, lotto1, lotto2


def daily_draws():
    """
    Return the daily draws
    """
    daily = Daily.objects.all()
    serializer = DailySerializer(daily, many=True)

    return JsonResponse(serializer.data, safe=False)
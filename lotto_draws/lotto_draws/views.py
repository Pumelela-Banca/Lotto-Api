"""
List of views for the lotto_draws app.
"""
from django.http import JsonResponse
from rest_framework import viewsets
from lotto_draws.models import (Daily, PowerBall, 
                    PowerBallPlus, Lotto, Lotto1, Lotto2)
from  lotto_draws.serializers import (DailySerializer, PowerBallSerializer, 
                            PowerBallPlusSerializer, LottoSerializer, 
                            Lotto1Serializer, Lotto2Serializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



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

def powerball_draws():
    """
    Return the powerball draws
    """
    powerball = PowerBall.objects.all()
    serializer = PowerBallSerializer(powerball, many=True)

    return JsonResponse(serializer.data, safe=False)

def powerball_plus_draws():
    """
    Return the powerball plus draws
    """
    powerball_plus = PowerBallPlus.objects.all()
    serializer = PowerBallPlusSerializer(powerball_plus, many=True)

    return JsonResponse(serializer.data, safe=False)

def lotto_draws():
    """
    Return the lotto draws
    """
    lotto = Lotto.objects.all()
    serializer = LottoSerializer(lotto, many=True)

    return JsonResponse(serializer.data, safe=False)

def lotto1_draws():
    """
    Return the lotto1 draws
    """
    lotto1 = Lotto1.objects.all()
    serializer = Lotto1Serializer(lotto1, many=True)

    return JsonResponse(serializer.data, safe=False)

def lotto2_draws():
    """
    Return the lotto2 draws
    """
    lotto2 = Lotto2.objects.all()
    serializer = Lotto2Serializer(lotto2, many=True)

    return JsonResponse(serializer.data, safe=False)

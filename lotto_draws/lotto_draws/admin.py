"""
Creating the admin interface for the lotto_draws app.
"""
from django.contrib import admin
from ..models import Daily, PowerBall, PowerBallPlus, Lotto, Lotto1, Lotto2

admin.site.register(Daily)
admin.site.register(PowerBall)
admin.site.register(PowerBallPlus)
admin.site.register(Lotto)
admin.site.register(Lotto1)
admin.site.register(Lotto2)

# predictor/forms.py
from django import forms

class PredictionForm(forms.Form):
    clubs = forms.IntegerField(label='Number of Clubs')
    players = forms.IntegerField(label='Number of Players')
    avg_age = forms.FloatField(label='Average Age')
    foreigners = forms.FloatField(label='Percentage of Foreigners')
    game_ratio_of_foreigners = forms.FloatField(label='Game Ratio of Foreigners')
    goals_per_game = forms.FloatField(label='Goals per Game')
    average_market_value = forms.FloatField(label='Average Market Value')

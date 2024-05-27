# predictor/views.py
from django.shortcuts import render
import pickle
import os
import pandas as pd
from .forms import PredictionForm

def predict_market_value(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract features from form
            clubs = form.cleaned_data['clubs']
            players = form.cleaned_data['players']
            avg_age = form.cleaned_data['avg_age']
            foreigners = form.cleaned_data['foreigners']
            game_ratio_of_foreigners = form.cleaned_data['game_ratio_of_foreigners']
            goals_per_game = form.cleaned_data['goals_per_game']
            average_market_value = form.cleaned_data['average_market_value']
            
            # Create DataFrame for prediction
            test_data = pd.DataFrame({
                'Clubs': [clubs],
                'Players': [players],
                'Avg Age': [avg_age],
                'Foreigners': [foreigners],
                'Game ratio of foreigners': [game_ratio_of_foreigners],
                'Goals per game': [goals_per_game],
                'Average Market value': [average_market_value]
            })
            
            # Load the trained model from the pickle file
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'football.pkl')
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)
            
            # Make prediction
            prediction = model.predict(test_data)[0]
            
            # Render the result
            return render(request, 'result.html', {'prediction': prediction})
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})

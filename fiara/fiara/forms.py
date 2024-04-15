from django import forms

from .models import Personne, Voiture


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ("id","nom", "prenom", "age", "genre")
        

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ("immatriculation", "marque", "proprietaire", "image")
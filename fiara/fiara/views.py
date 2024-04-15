from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import PersonneForm, VoitureForm
from .models import Personne, Voiture

def index(request):
    return render(request, "index.html")


def personne(request):
    if request.method == "GET":
        personnes = Personne.objects.all()
        context = {
            "form":PersonneForm(),
            "personnes": personnes
        }
        return render(request, "personne.html", context)
    elif request.method == "POST":
        data= PersonneForm(request.POST)
        if data.is_valid():
            nom_form= data.cleaned_data.get("nom")
            prenom_form= data.cleaned_data.get("prenom")
            age_form= data.cleaned_data.get("age")
            genre_form= data.cleaned_data.get("genre")
            personne= Personne.objects.create(nom= nom_form, prenom= prenom_form, age= age_form, genre= genre_form)
            personne.save()
            return redirect("personne")
        else:
            return HttpResponse("Form is not valid.")

def voiture(request):
    if request.method == "GET":
        voitures = Voiture.objects.all()
        context = {
            "form":VoitureForm(),
            "voitures":voitures
        }
        return render(request, "voiture.html", context)

    elif request.method == "POST":
        data= VoitureForm(request.POST)
        if data.is_valid():
            immatricule_form= data.cleaned_data.get("immatriculation")
            marque_form= data.cleaned_data.get("marque")
            proprietaire_form= data.cleaned_data.get("proprietaire")
            image_form= data.cleaned_data.get("image")
            voiture= Voiture.objects.create(immatriculation= immatricule_form, marque= marque_form, proprietaire= proprietaire_form, image= image_form)
            voiture.save()
            return redirect("voiture")
        else:
            return HttpResponse("Form is not valid.")
        
        
def supprimer_personne(request, id):
    Personne.objects.filter(id= id).first().delete()
    return redirect("personne") 

def supprimer_voiture(request, immatriculation):
    Voiture.objects.filter(immatriculation= immatriculation).first().delete()
    return redirect("voiture") 


def charger_personne(request, id):
    try:
        personne = Personne.objects.get(id=id)
        personne_data = {
            'id': personne.id,
            'nom': personne.nom,
            'prenom': personne.prenom,
            'age': personne.age,
            'genre': personne.genre
        }
        return JsonResponse(personne_data)
    except Personne.DoesNotExist:
        return JsonResponse({'error': 'Personne non trouvée'}, status=404)

def modifier_personne(request, id):
    try:
        personne = Personne.objects.get(id=id)
        if request.method == 'POST':
            form = PersonneForm(request.POST, instance=personne)
            if form.is_valid():
                form.save()
                return redirect('personnes')  # Assurez-vous que 'personnes' est correctement défini dans vos URLs
        else:
            form = PersonneForm(instance=personne)
        return render(request, 'modifier_personne.html', {'form': form, 'personne': personne})
    except Personne.DoesNotExist:
        return JsonResponse({'error': 'Personne non trouvée'}, status=404)
    

def charger_voiture(request, immatriculation):
    try:
        voiture = Voiture.objects.get(immatriculation= immatriculation)
        voiture_data = {
            'immatriculation': voiture.immatriculation,
            'marque': voiture.marque,
            'proprietaire': voiture.proprietaire,
            'image': voiture.image
        }
        return JsonResponse(voiture_data)
    except Personne.DoesNotExist:
        return JsonResponse({'error': 'Voiture non trouvée'}, status=404)

    
def modifier_voiture(request, immatriculation):
    voiture = Voiture.objects.get(immatriculation=immatriculation)
    if request.method == 'POST':
        form = VoitureForm(request.POST, instance=voiture)
        if form.is_valid():
            form.save()
            return redirect('voiture_list')
    else:
        form = VoitureForm(instance=voiture)
    return render(request, 'modifier_voiture.html', {'form': form})
from django.shortcuts import render
from.models import ChaiVarieties, Store
from django.shortcuts import get_object_or_404  # Import the ChaiVarieties model from the models.py file in the Chai app.  # Your models.py file is assumed to be in the same directory as the views.py file.  # Replace 'Chai' with the name of your app.  # Replace 'ChaiVarieties' with the name of your model.  # This line assumes that you have a ChaiVarieties model
from .forms import ChaiVarietiesForm


# Create your views here.
def all_chai(request):
    chais = ChaiVarieties.objects.all()
    return render(request, 'Chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarieties, pk=chai_id)
    return render(request, 'Chai/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    stores = None  # Initialize stores as None
    form = ChaiVarietiesForm()  # Initialize form for both GET and POST

    if request.method == 'POST':
        form = ChaiVarietiesForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']  # Correct variable name
            stores = Store.objects.filter(chai_varieties=chai_varity)  # Get matching stores
    
    return render(request, 'Chai/Chai_stores.html', {'stores': stores, 'form': form})



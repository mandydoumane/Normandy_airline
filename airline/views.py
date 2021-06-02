from django.shortcuts import render
from .forms import PageTwo, Pageone
from .models import Airport, Company, Flight, Booking, Plane, User

# Create your views here.

#  Formulaire de recherche de correspondance du vol du jour
def index(request):
    form=Pageone()
    if request.method=='POST':
        form = Pageone(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            depart = data['departure']
            arrive = data['arrival']
            dates = data['date']
            depart_id = Airport.objects.filter(city=depart).values()
            arrival_id = Airport.objects.filter(city=arrive).values()
            d_id = depart_id[0]['id']
            a_id = arrival_id[0]['id']
            vol = Flight.objects.filter(departure=d_id, arrival=a_id, date=dates).values()
            company = Company.objects.all().values()
            commodites = Plane.objects.all().values
            context = {'vol': vol, 'depart': depart, 'arrive': arrive, 'company': company, 'commodites': commodites}
            return render(request, 'booking.html', context)
    return render(request, 'index.html', {'form': form})


# Formulaire d'enregistrement du passager
def vol_resa(request, id):
    form=PageTwo()
    if request.method=='POST':
        form = PageTwo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user_exist = User.objects.filter(**data)
            obj = Flight.objects.get(id=id)
            if user_exist:
                Booking.objects.create(flight=obj, user=user_exist[0])
            else:
                User.objects.create(**data)
                user_exist = User.objects.filter(**data)
                Booking.objects.create(flight=obj, user=user_exist[0])
            return render(request, 'thanks.html')
    context = {'form': form}
    return render(request, 'name.html', context)

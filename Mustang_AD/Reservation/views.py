from pyexpat.errors import messages

from django.shortcuts import render


# Create your views here.
from Reservation.models import Reservation


def Reservations(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        bike = request.POST['bike']
        datefrm = request.POST['strt']
        dateto = request.POST['end']
        # fk_bike = Bikes.object.get()
        # fk_user = request.user.id
        obj = Reservation(Name=name, Email=email, Bike=bike, datefrom=datefrm, dateto=dateto)
        obj.save()
        current_user = request.user
        # messages.info(request, 'Booking successful please go to dasboard to view bookings')
    return render(request, 'Reservation.html')

from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="chennai"
    dest1.desc="Vanakam Chennai ugazhai anbudan varaverkeradhu"
    dest1.price =350
    dest1.img='destination_1.jpg'
    dest1.offer= False

    dest2=Destination()
    dest2.name="Coimbatore"
    dest2.desc="Vanakam Coimbatore ugazhai anbudan varaverkeradhu"
    dest2.price =650
    dest2.img='destination_2.jpg'
    dest2.offer= True
    dest3=Destination()
    dest3.name="Hyderabad"
    dest3.desc="Vanakam Hyderbad ugazhai anbudan varaverkeradhu"
    dest3.price =700
    dest3.img='destination_3.jpg'
    dest3.offer=True
    dests=[dest1,dest2,dest3]

    return render(request,"index.html",{'dests':dests})
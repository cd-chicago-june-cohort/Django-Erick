import django
from apps.dojo_ninjas.models import Dojo, Ninjas

#Create 3 dojos
Dojo.objects.create(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
Dojo.objects.create(name = 'CodingDojo Seattle', city = 'Seattle', state = 'WA')
Dojo.objects.create(name = 'CodingDojo New York', city = 'New York', state = 'NY')

#Create 3 ninjas that belong to the first dojo you created.
dojo = Dojo.objects.first()
Ninjas.objects.create(dojo = dojo, first_name = 'Erick', last_name = 'Ruiz')
Ninjas.objects.create(dojo = dojo, first_name = 'Gasper', last_name = 'Boy')
Ninjas.objects.create(dojo = dojo, first_name = 'Pablo', last_name = 'Picasso')

#Create 3 more ninjas and have them belong to the second dojo you created.
dojo = Dojo.objects.get(id = 2)
Ninjas.objects.create(dojo = dojo, first_name = 'Frida', last_name = 'Callo')
Ninjas.objects.create(dojo = dojo, first_name = 'Chumpy', last_name = 'Cat')
Ninjas.objects.create(dojo = dojo, first_name = 'John', last_name = 'Doe')

#Create 3 more ninjas and have them belong to the third dojo you created.
dojo = Dojo.objects.last()
Ninjas.objects.create(dojo = dojo, first_name = 'Josh', last_name = 'Boss')
Ninjas.objects.create(dojo = dojo, first_name = 'Bill', last_name = 'Nye')
Ninjas.objects.create(dojo = dojo, first_name = 'Neil', last_name = 'Tyson')

#Be able to retrieve all ninjas that belong to the first Dojo
dojo = Dojo.objects.first()
ninjas = Ninjas.objects.filter(dojo = dojo)
for ninja in ninjas:
    print ninja.first_name, ninja.last_name

#Be able to retrieve all ninjas that belong to the last Dojo
dojo = Dojo.objects.last()
ninjas = Ninjas.objects.filter(dojo = dojo)
for ninja in ninjas:
    print ninja.first_name, ninja.last_name
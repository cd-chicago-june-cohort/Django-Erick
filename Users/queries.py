import django
from apps.user_login.models import User

# Create a new model called 'User' with the information above.
# User.objects.create(first_name = 'Erick', last_name = 'Ruiz', email_address = 'erick_ruiz23@yahoo.com', age = 23)


#Know how to retrieve all users.
users = User.objects.all()
for user in users:
    print user.first_name, user.last_name, user.email_address
print('*') * 50

#Know how to get the first user.
first = User.objects.first()
print first.first_name, first.last_name
print('*') * 50

#Know how to get the last user.
last = User.objects.last()
print last.first_name, last.last_name
print('*') * 50

#Know how to get the users sorted by their first name (order by first_name DESC)
users = User.objects.order_by('-first_name')
for user in users:
    print user.first_name
print('*') * 50

#Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
user = User.objects.get(id=3)
print user.first_name, user.last_name
user.last_name = 'New Last Name'
user.save()
print user.first_name, user.last_name

#Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
User.objects.get(id = 4).delete()
users = User.objects.all()
for user in users:
    print user.first_name, user.last_name

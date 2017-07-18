import django
from apps.user.models import User

users = User.objects.all()
for user in users:
    print user.first_name, user.last_name, user.email

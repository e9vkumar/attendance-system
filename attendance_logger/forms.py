from django.contrib.auth.models import User

class Usercreation():
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

from django.forms import ModelForm
from .models import Squirrel
class SquirrelForm(ModelForm):
    class Meta:
        model=Squirrel
        field='__all__'




from django.forms import ModelForm
from app.models import Pelucia

# Create the form class.
class PeluciasForm(ModelForm):
    class Meta:
        model = Pelucia
        fields = ["modelo", "cor", "coracao", "tamanho","quantidade"]

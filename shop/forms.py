from django import forms
from .models import Review


""" class RegisterForm(forms.Form):

    email_address = forms.EmailField(label="Adresse Email:", required=True)
    pass_word = forms.CharField(label="Mot de passe:", required=True)

    first_name = forms.CharField(label="Nom", required=True)
    last_name = forms.CharField(label="Nom de famille", required=True)
    address = forms.CharField(label="Adresse", required=True)
    town = forms.CharField(label="Ville", required=True)
    postcode = forms.CharField(label="Code postale", required=True,
                               error_messages={"required": "REMPLIIIISS!!",
                                               "max_length": "Un code postale 
                                               a seulment 4 numero en Suisse!!!",
                                               })
    phone_number = forms.CharField(label="Téléphone", required=True) """


# ---- RENDER TROUGH FORM AND SAVE TROUGH MODELS -----

# We can use this class heritated from the **ModelForm** class to take same Fields from the models to use them
# in here for the forms!     It is like have a straight tunnel to store Data directly after the models.py fields.

# Of course we need to point to, which model we d'like to use, which model it should
# be related to it.       For that we use the NESTED META CLASS

# There we can add a "model property" to point at the model name we d'like to use.. import it!


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            "user_name": "nom d'utilisateur",
            "comment": "commentaire",
            "rating": "note"
        }

        error_messages = {
            "user_name": {
                "required": "Vous devez mettre un nom d'utilisateur",
                "max_length": "Vous avez dépassez le maximum de charactères possibles"
            },

            "comment": {
                "required": "Vous devez mettre un commentaire",
                "max_length": "Vous avez dépassez le maximum de charactères possibles"
            },

            "rating": {
                "required": "Vous devez mettre une note de 1 à 5"
            }
        }

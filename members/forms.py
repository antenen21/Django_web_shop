
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




# Create your forms here.   


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirmez le mot de passe", widget=forms.PasswordInput, required=True)
    street = forms.CharField(label="Adresse", help_text="Main-street 78", max_length=30, required=True)
    post_code = forms.CharField(label="Code postale", widget=forms.NumberInput())
    city = forms.CharField(label="Ville", required=True)
    province = forms.CharField(label="Canton", required=True)
    birth_date = forms.CharField(label="Date de naissance", widget=forms.DateInput(format='%d/%m/%Y'))


    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise forms.ValidationError("Ce nom d'utilisateur est déja utilisé par un autre client... Choissisez un autre.")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email = email)
        if new.count():
            raise forms.ValidationError("Cette adresse email est déjà occupé par un autre client...")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
            
        if password1 != password2:
            raise forms.ValidationError("Utilisez deux memes mot de passes!")
        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password2"],
        )
        return user
        
        


    





















""" class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'                                      # if we want to use all of them
    #   fields = ['user_name', 'last_name', 'address']          # field to set which one we want to use                   
    #   exclude = ['customer_comment']                          # if one modelField we want not to render but save it
                                   
        # NOTE at this point the rendering of the form names!!!! It does not automatically render the labels correctly and 
        # with the arguments we want, so we can use more property fields
        labels = {  "email_address":    "Adresse Email",
                    "pass_word":        "Mot de passe",
                    "first_name":       "Nom",
                    "last_name":        "Nom de famille",
                    "address":          "Adresse",
                    "town":             "Ville",
                    "postcode":         "Code Postale",
                    "phone_number":     "Numéro de télèphone"
        }
        error_messages = {
            "pass_word": {
                "required": "Il faut remplir  cette case...",
                "max_length": "Nobody will hack a password with 101 characters!!!",
            },
        
            # NOT WORKINGGGGGGGGGGGGG   
            "first_name": {
                "required": "Il faut remplir  cette case...",
                "max_length": "To many letters for a first name.. c'mon....",
            }
        } # We use the names of the model fields as keys, and as value we make a nested dictionary to enter the
          # different error messages """
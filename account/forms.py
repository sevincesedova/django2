from django import forms

class RegisterForm(forms.Form):
    SEX = [
    ('male', 'Kişi'),
    ('female', 'Qadın')
    ]
     

    name_surname=forms.CharField(max_length=50, label="Ad və soyad ")
    username=forms.CharField(max_length=50,label="İstifadəçi adi ")
    password=forms.CharField(max_length=10, min_length=5,label="Şifrə ", widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=10,min_length=5,label="Şifrəni təsdiqləyin ", widget=forms.PasswordInput)
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect, label="Cins ")
    birthday=forms.DateField(widget=forms.SelectDateWidget(years=range(2024,1900)))

    def clean(self):
        username=self.cleaned_data["username"]
        password=self.cleaned_data["password"]
        confirm=self.cleaned_data["confirm"]

        if password and confirm and password !=confirm:
            raise forms.ValidationError("Şifrələr eyni deyil.")
        
        values={
            "username":username,
            "password":password
        }

        return values
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,label="İstifadəçi adi ")
    password=forms.CharField(max_length=10, min_length=5,label="Şifrə ", widget=forms.PasswordInput)
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Введіть логін")
    password = forms.CharField(label="Введіть пароль", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="login")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    confirm = forms.CharField(label="confirm", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password != confirm:
            raise forms.ValidationError("Паролі не збігаються")

        values = {
            "username": username,
            "password": password
        }
        return values
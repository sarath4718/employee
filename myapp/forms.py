from django import forms
class EmployeeForm(forms.Form):

    name=forms.CharField()
    options=(
        ("Software Engineer","Software Engineer"),
        ("HR Manager","HR Manager"),
        ("Backend Developer","Backend Developer")
    )
    designation=forms.ChoiceField(choices=options)

    department=forms.CharField()

    contact=forms.CharField()

    salary=forms.IntegerField()

    address=forms.CharField()

from django import forms
from .models import Poll,Question


class form_poll_add(forms.ModelForm):

    choice1 = forms.CharField(label="first_choice",max_length=100,min_length=5 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    choice2 = forms.CharField(label="second_choice",max_length=100,min_length=5 ,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta :
        model = Poll
        fields = ['text','choice1','choice2']
        widgets = {'text':forms.Textarea(attrs={'class':'form-control',"rows":5 , 'col':20})}



class form_poll_edit(forms.ModelForm):



    class Meta:
        model = Poll
        fields = {"text"}
        widgets = {"text":forms.Textarea(attrs={'class':"form-control","row":5,"col":20})}



class form_add_choice(forms.ModelForm):



    class Meta :
        model = Question
        fields = {'choice_text'}
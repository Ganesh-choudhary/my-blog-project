from django import forms
class studentform(forms.ModelForm):
    F_name=forms.CharField(label='Enter the Your Name',max_length=200)
    L_name=forms.CharField(label='Enter the Your L_name',max_length=300)
    id_num=forms.CharField(label='Enter the Id_num',max_length=100)
    Email_id=forms.EmailField(label='Enter the Your Email_id',max_length=300)
    student_img=forms.ImageField()        

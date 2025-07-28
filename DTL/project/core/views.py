from django.shortcuts import render

# Create your views here.


def home(request):
    
    name='Sangamesh'
    age=20
    hobbies=['coding', 'reading', 'gaming']
    
    dict={
        'sname': name,
        'sage': age,
        'shobbies': hobbies,
        'fcolor':['green','red'],
        'ffood':'soya tofu',
        'collage':"prof.RMC akurdi "
    }
    
    
    return render(request, 'core/home.html',dict)
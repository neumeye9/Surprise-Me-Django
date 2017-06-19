from django.shortcuts import render, redirect
from random import shuffle
VALUES = ['cat', 'moose', 'flamingo', 'dog', 'hermit crab', 'elephant', 'sea otter', 'cow']

# Create your views here.

def index(request):
    return render(request, 'surpriseme_app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['num'] = request.POST['number']
        
        global VALUES
        shuffle(VALUES)
        return redirect('/surprises')


def surprises(request):
    num = int(request.session['num'])
    print num 
    if num <= len(VALUES):
        context = {
            'suprises' : VALUES[0:num]
        }
        return render(request, 'surpriseme_app/surprises.html', context)
    else:
        return redirect('/')
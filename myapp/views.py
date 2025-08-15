from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello! World.</h1>")
    #return render(request, 'index.html')

    #for dynamic contents:
    #name = "Yuvraj" or
    # we can define the context
    context = {
        'firstname': 'Bishal',
        'lastname' : 'Dhimal',
        'age' : '25',
        'nationality' : 'Nepalese'
    }
    #return render(request, 'index.html', {'name': name})
    return render(request, 'index.html', context)


def anotherurl(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'anotherurl.html', {'amount': amount_words})


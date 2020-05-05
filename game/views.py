from django.shortcuts import render

games=[
    {'name': 'Super Mario', 'price': 4.99 },
    {'name': 'Star Wars', 'price' : 5.99 }
]

def index(request):
    return render(request, 'game/index.html', context={'games': games})




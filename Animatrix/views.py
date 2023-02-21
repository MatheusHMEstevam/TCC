from django.shortcuts import render


# Create your views here.
def AnimatrixConfig(request):
    return render(request, 'pages/home/index.html')
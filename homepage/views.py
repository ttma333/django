from django.shortcuts import render

def landing(request):
   return render(
       request,
       'homepage/landing.html'
   )

def about_me(request):
    return render(
        request,
        'homepage/about_me.html'
    )

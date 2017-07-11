from django.shorcuts import render

def view(request):
return render(request, "home.html", {})
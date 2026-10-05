from django.http import HttpResponse


def home(request):
    return HttpResponse("Pagina de Home")


def about(request):
    return HttpResponse("Página de About")

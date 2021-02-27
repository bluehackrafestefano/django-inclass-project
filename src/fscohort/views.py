from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # print(request.GET)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # print(request.GET.get("q"))
    # return HttpResponse("Hello, Eda")
    my_context = {
        'title': 'clarusway',
        'dict_1': {'django': 'best'},
        'my_list': [1, 2, 3, 4],
    }
    return render(request, "fscohort/home.html", my_context)

def about_view(request):
    return HttpResponse("Hello, this is ABOUT PAGE")
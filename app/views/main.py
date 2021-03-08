from django.shortcuts import render

def main(request):

    data_dict = dict()

    return render(request, 'main.html', data_dict)
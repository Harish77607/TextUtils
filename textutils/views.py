# this is my file --- harish
from django.http import HttpResponse
from django.shortcuts import render
"""
#code for video -6 



def index(request):
    return HttpResponse('''<h1>hello this is harish</h1> <a href="https: // www.codewithharry.com/videos/python-django-tutorials-hindi-2">tutorials</a>''')


def about(request):
    return HttpResponse("this is about harish")
"""


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(djtext)
    #analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'Removed Punctuations',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed new Lines',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra spaces',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charcounter == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            analyzed += str(index)

        params = {'purpose': 'character count',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on" and spaceremover != "on" and charcounter != "on"):
        return HttpResponse('Please select any operation and try again')

    return render(request, 'analyze.html', params)


"""def analyze(request):
    pass

def capfirst(request):
    return HttpResponse('''capitalize first<br><a href="/">go to home</a>''')


def newlineremover(request):
    return HttpResponse("new line remover")


def spaceremover(request):
    return HttpResponse("space remover")
"""

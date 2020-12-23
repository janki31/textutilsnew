from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index2.html')

def analyze(request):
    # get value of text
    utext=request.POST.get('text')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    extraspace=request.POST.get('extraspace','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount=request.POST.get('charcount','off')
    print(utext)
    print(removepunc)

    if removepunc == "on":
        anayzetext = ""
        punc='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in utext:
            if char not in punc:
                anayzetext=anayzetext+char
        utext=anayzetext

    if fullcaps=="on":
        anayzetext = ""
        for char in utext:
            anayzetext=anayzetext+char.upper()
        utext = anayzetext

    if extraspace=="on":
        anayzetext = ""
        for index,char in enumerate(utext):
            if not(utext[index]==" "):
                anayzetext=anayzetext+char
        utext = anayzetext

    if newlineremover=="on":
        anayzetext = ""
        for char in utext:
            if char!='\n' and char!='\r':
                anayzetext=anayzetext+char
        utext = anayzetext

    if charcount=="on":
        anayzetext = ""
        count=0
        for char in utext:
            print(char.isdigit())
            if (char !=' ' and char.isdigit()!=True):
                count+=1
        anayzetext=utext+"\nTotal Character:- "+str(count)

    if(removepunc != "on" or fullcaps!="on" or extraspace!="on" or newlineremover!="on"
            or charcount!="on" ):
        anayzetext="Please Select Proper Operation to utilize your text"


    params = {'anayzetext': anayzetext}
    return render(request,'analyze2.html',params)
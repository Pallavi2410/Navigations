from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':105 ,'b':210 }
    return render(request ,'a1_first.html', d)

def a1_secound(request):
    d={'a':101 ,'b':103 ,'c':190}
    return render(request ,'a1_secound.html' ,d)
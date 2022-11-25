from django.shortcuts import render

# Create your views here.
def  a2_first(request):
    d={'a': 102 ,'b':100,'c':150}
    return render(request, 'a2_first.html', d)

def a2_secound(request):
    d={'name':'Pallavi'}
    return render(request, 'a2_secound.html', d)
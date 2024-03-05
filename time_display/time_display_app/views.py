from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%B %d, %Y", localtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request,'index.html', context)
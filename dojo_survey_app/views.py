from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method != "POST":
        return redirect('/')
    request.session['fullname'] = request.POST['fullname']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect(f'/results')

def results(request):
    return render(request, 'results.html')

def clear_session(request):
    request.session.flush()
    return redirect('/')

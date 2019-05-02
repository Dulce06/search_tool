from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.shortcuts import redirect

# Create your views here.

def index(request):
    data = open('exercise-data.json').read()
    jsonData_loaded = json.loads(data)
    for item in jsonData_loaded:
        item['job_history'] = ','.join(item['job_history'])

    # return HttpResponse(jsonData_loaded)
    return render(request, "index.html", {'jsondata':jsonData_loaded})

def email(request):
    data = open('exercise-data.json').read()
    jsonData_loaded = json.loads(data)
    for item in jsonData_loaded:
        item['job_history'] = ','.join(item['job_history'])

    # return HttpResponse(jsonData_loaded)
    return render(request, "email.html", {'jsondata':jsonData_loaded})

def city(request):
    data = open('exercise-data.json').read()
    jsonData_loaded = json.loads(data)
    for item in jsonData_loaded:
        item['job_history'] = ','.join(item['job_history'])

    # return HttpResponse(jsonData_loaded)
    return render(request, "city.html", {'jsondata':jsonData_loaded})

def name(request):
    data = open('exercise-data.json').read()
    jsonData_loaded = json.loads(data)
    for item in jsonData_loaded:
        item['job_history'] = ','.join(item['job_history'])

    # return HttpResponse(jsonData_loaded)
    return render(request, "name.html", {'jsondata':jsonData_loaded})

def country(request):
    data = open('exercise-data.json').read()
    jsonData_loaded = json.loads(data)
    for item in jsonData_loaded:
        item['job_history'] = ','.join(item['job_history'])

    # return HttpResponse(jsonData_loaded)
    return render(request, "country.html", {'jsondata':jsonData_loaded})

def search_company(request):
    key_word = request.POST['company']
    if key_word == "":
        return redirect('index')
    else:
        new_list = []
        data = open('exercise-data.json').read()
        jsonData_loaded = json.loads(data)
        for item in jsonData_loaded:
            if key_word.lower() in item['company'].lower():
                new_list.append(item)
        for listitem in new_list:
            listitem['job_history'] = ','.join(listitem['job_history'])
        # return HttpResponse(new_list)
        return render(request, "index.html", {'jsondata': new_list})

def search_email(request):
    key_word = request.POST['email']
    if key_word == "":
        return redirect('email')
    else:
        new_list = []
        data = open('exercise-data.json').read()
        jsonData_loaded = json.loads(data)
        for item in jsonData_loaded:
            if key_word.lower() in item['email'].lower():
                new_list.append(item)
        for listitem in new_list:
            listitem['job_history'] = ','.join(listitem['job_history'])
        # return HttpResponse(new_list)
        return render(request, "email.html", {'jsondata': new_list})

def search_city(request):
    key_word = request.POST['city']
    if key_word == "":
        return redirect('city')
    else:
        new_list = []
        data = open('exercise-data.json').read()
        jsonData_loaded = json.loads(data)
        for item in jsonData_loaded:
            if key_word.lower() in item['city'].lower():
                new_list.append(item)
        for listitem in new_list:
            listitem['job_history'] = ','.join(listitem['job_history'])
        # return HttpResponse(new_list)
        return render(request, "city.html", {'jsondata': new_list})

def search_name(request):
    key_word = request.POST['name']
    if key_word == "":
        return redirect('name')
    else:
        new_list = []
        data = open('exercise-data.json').read()
        jsonData_loaded = json.loads(data)
        for item in jsonData_loaded:
            if key_word.lower() in item['name'].lower():
                new_list.append(item)
        for listitem in new_list:
            listitem['job_history'] = ','.join(listitem['job_history'])
        # return HttpResponse(new_list)
        return render(request, "name.html", {'jsondata': new_list})

def search_country(request):
    key_word = request.POST['country']
    if key_word == "":
        return redirect('country')
    else:
        new_list = []
        data = open('exercise-data.json').read()
        jsonData_loaded = json.loads(data)
        for item in jsonData_loaded:
            if key_word.lower() in item['country'].lower():
                new_list.append(item)
        for listitem in new_list:
            listitem['job_history'] = ','.join(listitem['job_history'])
        # return HttpResponse(new_list)
        return render(request, "country.html", {'jsondata': new_list})

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import mysql.connector

def index(request):
    return render(request, 'quoteCalculator/index.html')
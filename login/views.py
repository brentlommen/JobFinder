from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import loginForm
import mysql.connector

# Create your views here.

def index(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            cursor.execute("SELECT companyId FROM users WHERE email = '" + data['email'] + "' AND password = '" + data['password'] +"'")
            user = cursor.fetchall()
            if cursor.rowcount == 1 :
                return HttpResponseRedirect('/availableJobs/'+ str(user[0][0]))
            else :
                form = loginForm()
                return render(request, 'login/index.html', {'form': form})
        else :
            form = loginForm()
            return render(request, 'login/index.html', {'form': form})
    else:
        form = loginForm()
        return render(request, 'login/index.html', {'form': form})
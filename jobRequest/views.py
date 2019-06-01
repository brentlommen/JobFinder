from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .form import bookingForm
import mysql.connector

def index(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    if request.method == 'POST':
        form = bookingForm(request.POST)

        if form.is_valid():
            print("test")
            data = form.cleaned_data
            cursor.execute("INSERT INTO jobs( categoryId, clientEmail, clientAddress, available, type, bookingDate) "+
                                "VALUES ('1','" + data["email"] + "','" + data["address"]  + "', '1' , '" + data['service'] + "','" + str(data['date']) + "' )")
            conn.commit()

    else :
        form = bookingForm()


    return render(request, 'jobRequest/index.html', {'form': form})
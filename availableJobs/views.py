from itertools import count

from django.http import HttpResponseRedirect
from django.shortcuts import render
import mysql.connector

def index(request,company_id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    cursor.execute("SELECT clientName, clientAddress, type, clientEmail, id FROM jobs WHERE available = TRUE")
    availableJobs = cursor.fetchall()
    context = {
        'availableJobs' : availableJobs,
        'companyId' : company_id,
    }
    print(availableJobs)

    conn.close()
    cursor.close()
    return render(request, 'availableJobs/index.html', context)

def addJob(request, company_id, job_id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    cursor.execute("UPDATE jobs set available = FALSE, companyId = '" + str(company_id) + "' WHERE id = '" + str(job_id) + "'")
    conn.commit()

    conn.close()
    cursor.close()
    return HttpResponseRedirect("/availableJobs/" + str(company_id) + "/activeJobs/")

def removeJob(request, company_id, job_id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    cursor.execute("UPDATE jobs set available = TRUE, companyId = NULL WHERE id = '" + str(job_id) + "'")
    conn.commit()

    conn.close()
    cursor.close()

    return HttpResponseRedirect("/availableJobs/" + str(company_id) + "/activeJobs/")

def activeJobs(request, company_id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='jobfinder')
    cursor = conn.cursor()

    cursor.execute("SELECT clientName, clientAddress, type, description, clientEmail, id FROM jobs WHERE companyId = '" + str(company_id) + "'")
    activeJobs = cursor.fetchall()

    context = {
        'activeJobs' : activeJobs,
    }

    return render(request, 'availableJobs/activeJobs.html', context)

def contact(request, company_id, job_id):
    return render(request, 'availableJobs/contact.html')

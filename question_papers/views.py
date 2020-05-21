#       python manage.py runserver

from django.shortcuts import render, HttpResponse
from .models import Question_papers
from django.http import request
# from .filters import Question_papersfilter
# Create your views here.

def colleges(request):
    allqp=Question_papers.objects.order_by('college').distinct('college')
    # college= Question_papers.objects.filter('college')
    context={'allqp' : allqp,'Select':'Select Your Current Education : '}
    return render(request,'qp.html',context)

def college(request,college):
    college=Question_papers.objects.filter(college=college).order_by('university').distinct('university')
    college={'college' : college}
    print(college)
    return render(request,'qp.html',college)

def university(request,college,university):
    university=Question_papers.objects.filter(university=university,college=college).order_by('course').distinct('course')
    university={'university' : university}
    print(university)
    return render(request,'qp.html',university)

def course(request,college,university,course):
    course=Question_papers.objects.filter(course=course, university=university).order_by('year').distinct('year')
    course={'course' : course}
    print(course)
    return render(request,'qp.html',course)

# 
# 
def year(request,college,university,course,year):
    year=Question_papers.objects.filter(course=course,university=university).order_by('subject').distinct('subject')
    year={'year':year}
    return render(request,'qp.html',year)

def question_papers(request,college,university,course,year,subject):
    papers=Question_papers.objects.filter(subject=subject,university=university).order_by('course','subject','year').distinct('course','subject','year')
    papers={'paper':papers}
    return render(request,'qp.html',papers)

# def pdf_view(request,college,course,year,subject,id):
#     pdf=Question_papers.objects.get(id=id)
#     with open('pdf.pre_year_papers', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=pdf.pre_year_papers'
#         return response
#     pdf.closed
   
# def filter(request):
    # filter=Question_papers.objects.all()
    # myfilter= Question_papersfilter()
    # filter={ 'myfilter':myfilter}
    # return render(request,'qp.html',filter)

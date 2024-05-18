
from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

from django.http import HttpResponseNotFound
from django.shortcuts import render,redirect
from blog.forms import studentform
from blog.functions.functions import handle_uploaded_file
#from django.views.decorators.http import require_http_method
import datetime as d

def about_us(request):
    return HttpResponse("<h1>weleome to my about page</h1>")

def gallary(request):
    return render(request,'index1.html')

def check_my(request):
    return render(request,'index.html')
def home_(request):
    data={
        'title': 'Home-page',
        'list' : ["python","Java","django"],
        'number':[],

        'student' : [
         
        {'name':'ganesh choudhary','phone':"9302647988"},
        {'name': 'Radhe savnar','phone':'7828394090'}

        ]

    }
    return render(request,"myFirst.html", data)

def Course(request):
    return HttpResponse("welcome to my Courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def contact(request):
    array = {
       'lis1' : ['hello','ganesh']
    }

    return render(request,'second.html',array)

'''
def now_time(request):
    now = datetime.datetime.now()
    html=("Times nows-:{}".format(now))
    return HttpResponse(html)
'''
def aboutUs(request):
    data = {
        "title":"Hello-page",
        "dt" : "welcome to my Webpages-:",
        "list1" : [ "python","html","css","javaScripts","BootScripts"],
        
        "student" : [

                    {"name":"ganesh", "last_name":"choudhary", "phone": 9302647988},
                    {"name":"Khushi", "last_name":"savaner", "phone":9302647988}
        ],

        "x":[]  

    }
    return render(request, "home.html",data)


def gallaryUs(request):
    data ={
        "title":"Your Welcome for Me",
    "text":"Om Namah Bhagvate vashudevai namah-:",
    "input":[
        "Python","Java","c++","c","Html","Css","Java Scripts"
    ],
    }
    return render(request, "index.html",data)

def home(request):
    return HttpResponse("Hello My Function-:")

def home_d(request,course_id):
    return HttpResponse(course_id)

def current_datetime(request):
    now=d.datetime.now()
    html=("This is Current Datetime-:{}".format(now))
    return HttpResponse(html)

def hello(request):
    return HttpResponse("<h1>Hello-World</h1>")

def product(request):
    k="<h1>ganesh choudhary</h1>"
    return HttpResponse(k)

def product_Id(request,product_Id):
    return HttpResponse(product_Id)


def check_data(request):
    if request.method=='POST':
        form=studentform(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
        return HttpResponse('File Uploaded Seccuss Fully')
    else:
        form=studentform()
    return render(request,'cust_info.html',{'form':form})

'''
def Learner_img(request):
    if request.method=='POST':
        form=Learner_deta(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            form=studentform()
    return render(request,'learner_info.html',{'form':form})

def success(request):
    return HttpResponse('Successfully uploaded')
'''


def course_details(request,courseid):
    return HttpResponse(courseid)

def index_page(request):
    return render(request, "index2.html")

def contact_page(request):
    return render(request,"contact.html")

def archive_page(request):
    return render(request,"archive.html")
def single_page(request):
    return render(request,"single.html")

def product(request):
    return HttpResponse('<h1>Hello-page<h1>')

def product_id(request,product_id):
    return HttpResponse(product_id)


def check(request):
    return HttpResponse('<h1>Hello-Page</h1>')
def data(request):
    temp=loader.get_template('text1.html')
    name={
        'Stundet':'Ganesh',
        'Skills' : 'Python, Java',
        'Id_num' : '2',
        'contanct' : '99888'
    }
    return HttpResponse(temp.render(name))

def index(request):
    return render(request,'text1.html')



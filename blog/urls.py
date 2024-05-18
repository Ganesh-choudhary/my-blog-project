
from django.urls import path

from .import views

urlpatterns = [
    path("gallary/",views.gallary,name="funo"),
    path("contact/",views.contact, name="about_US"),
    path("",views.about_us,name="About-page"),
    path("check_my/",views.check_my,name="my_check"),
    path("course/",views.Course, name="Course-information"),
    path("course/<courseid>",views.courseDetails),
    path("home_/",views.home_,name="Home-page"),

    path('check_data',views.check_data,name="img Uploaded Check"),

    path("", views.hello, name="Hello-world"),
    
    path("product", views.product, name="chek function"),
    path("product/<str:product_Id>", views.product_Id, name="Product_Details"),
    
    path("",views.aboutUs, name="AboutUs-Page" ),
    path("index_page/",views.index_page,name="Indexing pages"),
    path("gallaryUs/",views.gallaryUs, name="GallaryUs"),
    path("home/", views.home, name="Home-page"),
    path("now_time/",views.now_time,name="Date-time"),
    path("current_datetime/",views.current_datetime,name="Current Date-time"),

    path("course/<courseid>", views.course_details, name="Course Details-:"),
    path("home/<course_id>",views.home_d,name="dynamic pages-:"),

    path("product", views.product, name="chek function"),
    path("product/<product_id>", views.product_id, name="Product_Details"),
    path("contact_page/", views.contact_page,name="Conatac-pages"),
    path("archive_page/", views.archive_page,name="Archivement-pages"),
    path("single_page/",views.single_page,name="Single page Views"), 
    path("product",views.product,name="check-Data"),
    path('product/<product_id>',views.product,name="dataDetails"),
    path('check/',views.check,name='check-data'),
    path('data/',views.data,name='my-datapage'),
    path('index/',views.index,name='index-page'),
]

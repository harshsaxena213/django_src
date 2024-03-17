from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[{"name":"harsh","age":12,"occupation":"Student"},{"name":"aaryan","age":22,"occupation":"student"},{"name":"shlok","age":10,"occupation":"simp"}]    

    for people in peoples:
        print(people)

    student_attendence_data=[{"name":"harry","name":"good","name":"shit"}]



    text="""admfhuoiwevbuio nfv0iqeu09fv u09wqe b f09ubewvewbu f90wgbu89t0ghwvbfuiowhctf8u9r
        """
    
    random_lsit=["harsh",21,"WhoKnows","Eminem",69]
    return render(request ,"index.html", context={'peoples':peoples,'text':text,'random_lsit':random_lsit})
def success_page(request):
    print("Hellow 10 Times")
    return HttpResponse("<h1>Success Page</h1>")
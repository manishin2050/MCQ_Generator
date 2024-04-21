from django.shortcuts import render,redirect,HttpResponse
from website.models import MCQ_Gen,QuizHeading

# Create your views here.
def home(request):
    context={
        "data":QuizHeading.objects.order_by('-id')
    }

    if request.method=="POST":
        name=request.POST.get('name')
        # print(name)
        if name !='':
            Quiz=QuizHeading(name=name)
            Quiz.save()

        return redirect('/')
    return render(request,"home.html",context)
def index(request,id):
    context={

        "data":MCQ_Gen.objects.filter(code=id),
        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    if request.method=="POST":
        que=request.POST.get('que')
        code=id
        ans=request.POST.get('ans')
        opt1=request.POST.get('opt1')
        opt2=request.POST.get('opt2')
        opt3=request.POST.get('opt3')
        opt4=request.POST.get('opt4')
        Data= MCQ_Gen(que=que,code=code,ans=ans,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4)
        Data.save()
        return redirect(f'/index/{id}')
    return render(request,'index.html',context)

def questions(request,id):
    context={
        "data":MCQ_Gen.objects.filter(code=id),
        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    return render(request,'questions.html',context)

def quiz_delete(request,id):

    QuizHeading.objects.get(id=id).delete()
    for i in MCQ_Gen.objects.filter(code=id):
        i.delete()

    return redirect('/')

def quiz_edit(request,id):
    context={

        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    if request.method=="POST":
        name=request.POST.get('name')
        Data= QuizHeading(id=id,name=name)
        Data.save()
        return redirect(f'/index/{id}')

    return render(request,"quiz_edit.html",context)

def que_edit(request,id):
    code=MCQ_Gen.objects.get(id=id).code
    # print(code)
    context={
        "name":QuizHeading.objects.get(id=code).name,
        "id":id,
        "que":MCQ_Gen.objects.get(id=id).que,
        "ans":MCQ_Gen.objects.get(id=id).ans,
        "opt1":MCQ_Gen.objects.get(id=id).opt1,
        "opt2":MCQ_Gen.objects.get(id=id).opt2,
        "opt3":MCQ_Gen.objects.get(id=id).opt3,
        "opt4":MCQ_Gen.objects.get(id=id).opt4,
        "code":MCQ_Gen.objects.get(id=id).code,

    }
    if request.method=="POST":
        que=request.POST.get('que')
        code= request.POST.get('code')
        ans=request.POST.get('ans')
        opt1=request.POST.get('opt1')
        opt2=request.POST.get('opt2')
        opt3=request.POST.get('opt3')
        opt4=request.POST.get('opt4')
        Data= MCQ_Gen(id=id,que=que,code=code,ans=ans,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4)
        Data.save()
        return redirect(f'/index/{code}')

    return render(request,"que_edit.html",context)

def que_delete(request,id):
    code=MCQ_Gen.objects.get(id=id).code
    MCQ_Gen.objects.get(id=id).delete()
    return redirect(f"/index/{code}")
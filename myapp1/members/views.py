from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from members.models import members_q_a  # Must match the model class name
from . models import members_q_a
from . models import regform
from django.urls import reverse







def members(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def register(request):
    template=loader.get_template('registrationform.html')
    return HttpResponse(template.render())

def registerdb(request):
    fn=request.GET.get("fname")
    ln=request.GET.get("lname")
    g=request.GET.get("gender")
    d=request.GET.get("dob")
    pn=request.GET.get("mobile")
    e=request.GET.get("email")
    un=request.GET.get("su_name")
    ps=request.GET.get("su_pass")
    details=regform(fname=fn,lname=ln,gender=g,dob=d,phone=pn,email=e,uname=un,passcode=ps)
    details.save()
    template=loader.get_template('login.html')
    return redirect('quiz:login')
    


def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

def logindb(request):
    un=request.GET.get("uname")
    pa=request.GET.get("pass")
    check = regform.objects.filter(uname=un,passcode=pa).values()
    if check:
        return redirect(reverse('quiz:subject'))
        
    else:
        template=loader.get_template('login.html')
        context = {'result':'Incorrect username or password,try again',}
        return HttpResponse(template.render(context,request))
    
def subject(request):
    return render(request, 'subject.html')


def sub_ch(request):
    '''
    selected_subject = request.GET.get("subject")
    print("Subject:", selected_subject)
    
    if selected_subject == 'science':
        return redirect('quiz:science')
    elif selected_subject == "aptitude":
        return redirect('quiz:record')
    else:
        return render(request, 'subject.html', {'result': 'please choose any subject'})
    '''
    subject = request.GET.get('subject')
    if subject == 'science':
        return redirect(reverse('quiz:science'))  # or render science template
    elif subject == 'aptitude':
        return redirect('record')   # or render aptitude template

def science(request):
    score=0
    if "score" in request.GET:
        score=int(request.GET["score"])
    if "submit2" in request.GET:
        result=loader.get_template('result.html')
        con = {'myresult':result,'score':score,}
        return HttpResponse(result.render(con,request))
    else:
        template=loader.get_template('subject.html')
        a=0
        if "id_text" in request.GET:
            a=int(request.GET.get("id_text"))       
        if "op" in request.GET:
            check = request.GET.get(f"op_{a}")

            correct=members_q_a.objects.filter(id=a).values_list('answer',flat=True).first()
            if check==correct:
                score+=1
        a+=1   
        elements = members_q_a.objects.filter(id=a).values()
        context = {'myelements':elements,'score':score,}
        return HttpResponse(template.render(context,request))
       


def record(request):
    score=0
    if "score" in request.GET:
        score=int(request.GET["score"])
    if "submit2" in request.GET:
        result=loader.get_template('result.html')
        con = {'myresult':result,'score':score,}
        return HttpResponse(result.render(con,request))
    else:
        template=loader.get_template('subject.html')
        a=0
        if "id_text" in request.GET:
            a=int(request.GET.get("id_text",1))       
        if "op" in request.GET:
            check = request.GET.get(f"op_{a}")

            correct=members_q_a.objects.filter(id=a).values_list('answer',flat=True).first()
            if check==correct:
                score+=1
        a+=1   
        elements =members_q_a.objects.filter(id=a).values()         
        context = {'myelements':elements,'score':score,}
        return HttpResponse(template.render(context,request))
    
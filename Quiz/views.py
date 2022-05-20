from django.shortcuts import render, redirect, get_object_or_404
from .models import Question,EndUser,Answer
from django.core.paginator import Paginator

def home(request):
    if request.GET:
        user = EndUser()
        user.name = request.GET['name']
        if request.GET['name'] =="":
            user.name="익명"
        user.save()
        return redirect("quiz",user.pk)
    return render(request,"home.html")

def quiz(requset,pk):
    user = get_object_or_404(EndUser,pk=pk)
    aans = get_object_or_404(Answer)

    num = 1
    if requset.POST:
        num = int(requset.POST['quiz_id']) + 1
        user.answer = user.answer + requset.POST['answer']
        if requset.POST['answer'] == aans.ans[num-2]:
            user.score = user.score + 1
            user.save()

        if num > len(aans.ans):
            return redirect("result",pk)

    quiz = get_object_or_404(Question, id=num)
    return render(requset, "quiz.html", {'quiz':quiz})

def result(requset, pk):
    user = get_object_or_404(EndUser, pk=pk)

    all_user = EndUser.objects.all()
    scorelist = []
    for i in all_user:
        each_score = i.score
        scorelist.append(each_score)
    average_score = round(sum(scorelist)/len(all_user))
    if len(user.answer) == 10:
        while True:
            try:
                pass
                break
            except:
                return requset(requset,'error.html')

    return render(requset,"result.html",{"user":user,'average_score':average_score})

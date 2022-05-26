from django.shortcuts import render, redirect, get_object_or_404
from .models import Question,EndUser,Answer
from django.core.paginator import Paginator

def home(request):
    if request.GET:
        user = EndUser()
        user.name = request.GET['name']

        if request.GET['name'] == "":
            user.name="익명"
            user.save()
            return redirect("quiz",user.pk)

        elif request.GET['name'] != "" and request.GET['name'] != "addition":
            user.name = request.GET['name']
            user.save()
            return redirect("quiz", user.pk)

        elif request.GET['name'] == "addition":
            return redirect("add")

    return render(request,"home.html")

def quiz(requset,pk):
    user = get_object_or_404(EndUser,pk=pk)
    t_ans = get_object_or_404(Answer)
    r_tmp = []
    num = 1
    if requset.POST:
        num = int(requset.POST['quiz_id']) + 1
        user.answer = user.answer + requset.POST['answer']
        user.save()

        if requset.POST['answer'] == t_ans.ans[num-2]:
            user.score = user.score + 1
            user.save()

        elif requset.POST['answer'] != t_ans.ans[num-2]:
            r_tmp.append(num)

        if num > len(t_ans.ans):
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

    return render(requset,"result.html",{"user":user,'average_score':average_score})

def add(request):
    if request.GET:
        q = Question()
        a = get_object_or_404(Answer)
        q.question = request.GET['quiz']
        q.option1 = request.GET['option1']
        q.option2 = request.GET['option2']
        q.option3 = request.GET['option3']
        q.option4 = request.GET['option4']
        a.ans = a.ans + request.GET['answer']
        q.save()
        a.save()

    return render(request,"add.html")

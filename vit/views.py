from django.contrib.auth.decorators import login_required
from .models import *

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'vit/index.html')


@login_required()
def stud(request):
    y = request.user
    posts = Student.objects.filter(regno__iexact=y.username)
    out = Outing.objects.filter(regno=y.username)
    marks1 = Enrolled.objects.filter(regno=y.username, semester=1).select_related('cid')
    marks2 = Enrolled.objects.filter(regno=y.username, semester=2).select_related('cid')
    marks3 = Enrolled.objects.filter(regno=y.username, semester=3).select_related('cid')
    marks4 = Enrolled.objects.filter(regno=y.username, semester=4).select_related('cid')
    lib = Borrow.objects.filter(memid=y.username).select_related('bookid').values('bookid__bookid', 'bookid__bname',
                                                                                  'issuedate', 'duedate', 'returndate',
                                                                                  'id')

    hos = Student.objects.filter(regno=y.username).select_related('hid').values('hid__block', 'hid__roommo__roomno',
                                                                                'hid__roommo__type',
                                                                                'hid__roommo__nbeaded')

    att = Take.objects.filter(regno=y.username).select_related('clid').values('clid__cid__cname', 'attendence', 'date',
                                                                              'id')
    att2 = Take.objects.filter(regno=y.username).select_related('clid').values('clid__cid__cname')
    myc = Take.objects.filter(regno=y.username).select_related('clid').values('clid__cid__cname', 'clid__startime',
                                                                              'clid__endtime',
                                                                              'clid__day').distinct().order_by(
        'clid__day', 'clid__startime')

    acc = Account.objects.filter(regno=y.username)
    mat = Material.objects.all().values('cid__cname', 'title', 'mat', 'fid__fname', 'date')

    si = int(len(att2))
    su = []
    for i in range(si):
        qu = Take.objects.select_related('clid').filter(regno=y.username, clid__cid__cname=att2[i]['clid__cid__cname'])
        su.append(qu)

    # for calculating grade
    l1 = []
    for q in marks1:
        a = float(q.cat1 + q.cat2 + q.ass1 + q.ass2 + q.ass3 + q.fat)
        a = round(a / 9.5, 2)
        l1.append(a)
    grade1 = sum(l1)
    if len(marks1) != 0:
        grade1 = round(grade1 / len(marks1), 2)

    l2 = []
    for q in marks2:
        a = float(q.cat1 + q.cat2 + q.ass1 + q.ass2 + q.ass3 + q.fat)
        a = round(a / 9.5, 2)
        l2.append(a)
    grade2 = sum(l2)
    if len(marks2) != 0:
        grade2 = round(grade2 / len(marks2), 2)

    l3 = []
    for q in marks3:
        a = float(q.cat1 + q.cat2 + q.ass1 + q.ass2 + q.ass3 + q.fat)
        a = round(a / 9.5, 2)
        l3.append(a)
    grade3 = sum(l3)
    if len(marks3) != 0:
        grade3 = round(grade3 / len(marks3), 2)

    l4 = []
    for q in marks4:
        a = float(q.cat1 + q.cat2 + q.ass1 + q.ass2 + q.ass3 + q.fat)
        a = round(a / 9.5, 2)
        l4.append(a)
    grade4 = sum(l4)
    if len(marks4) != 0:
        grade4 = round(grade4 / len(marks4), 2)

    k = {'s': posts, 'marks1': marks1, 'marks2': marks2, 'marks3': marks3, 'marks4': marks4, 'z': grade1, 'z2': grade2,
         'z3': grade3, 'z4': grade4, 'out': out, 'lib': lib, 'hos': hos, 'att': att, 'myc': myc, 'acc': acc, 'mat': mat}

    return render(request, 'vit/stud.html', k)


def login(request):
    return render(request, 'vit/login.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('http://127.0.0.1:8000/vit/change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'vit/change.html', {'form': form})

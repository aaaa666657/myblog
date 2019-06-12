
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,  get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages,auth
from .models import Post,Teacher,ClassTable
from .forms import UserCreationForm
from .forms import User


import pandas as pd
import urllib.parse

# Create your views here.
def teacher_list(request):
    if request.user.is_authenticated:
        teacher = Teacher.objects.all()
        storage = messages.get_messages(request)
        return render(request,
         'blog/post_list.html',
          {
            'teachers': teacher,
            'messages':storage,
            'username':auth.get_user(request).username
          })
    else: 
        return redirect('login')


def addteacher(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:    
            if request.method == "POST":
                new_title   = request.POST.get('name')
                if not Teacher.objects.filter(name=new_title):
                    new_teacher = Teacher(name=new_title)
                    url = "https://www.iecs.fcu.edu.tw/teacher/"+urllib.parse.quote(new_title)+"/class/"
                    try:
                        dfs = pd.read_html(url)  ## 回傳DataFrame類別的陣列
                        df = dfs[1]
                        df  = [ row[1:] for row in df.values.tolist()]
                        new_teacher.save()
                        for i in range(14):
                            for j in range(7):
                                if df[i][j] != '-':
                                    ClassTable(name=df[i][j],weekday=j,period=i,teacher=new_teacher).save()
                    except:
                        messages.add_message(request, messages.WARNING, '資訊系無此教授')
                    return redirect('teacher_list')
                else:
                    messages.add_message(request, messages.WARNING, '已有此老師')
                    return redirect('teacher_list')
            return render(request, 'teacher_create.html', {})
        else:
            messages.add_message(request, messages.WARNING, '您無此權限')
            return redirect('teacher_list')
    else: 
        return redirect('login')

class UserCreate(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        messages.success(self.request, '帳戶已創立')
        return reverse('login')

def showclass(request):
    if request.user.is_authenticated:
        name = request.GET.get('name')
        try:
            teacher = Teacher.objects.get(name=name)
        except Teacher.DoesNotExist:
            pass
        else:
            klass = ClassTable.objects.filter(teacher=teacher).order_by('period','weekday')
            klass = list(klass)
            htmlcode = '<table style="border:3px #FFD382 dashed;" cellpadding="10" border="1">\n'
            htmlcode += '<th><td>星期一</td><td>星期二</td><td>星期三</td><td>星期四</td><td>星期五</td><td>星期六</td><td>星期日</td></th>\n'
            for j in range(14):
                htmlcode += '<tr><td>第'+str(j+1)+'節</td>'
                for i in range(7):
                    if klass and klass[0].weekday == i and  klass[0].period == j:
                        htmlcode += '<td>'+klass[0].name+'</td>'
                        klass.pop(0)
                    else:
                        htmlcode += '<td>      </td>'
                htmlcode += "</tr>\n"
            htmlcode += "\n"
            htmlcode += '</table>'

            return render(request,'klass.html', {'name': name ,'klasses': klass,'htm1':htmlcode})
    else: 
        return redirect('login')    
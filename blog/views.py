from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,  get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Post
from .forms import UserCreationForm
from .forms import User

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_create(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        new_post = Post(title=new_title, text=new_text)

        new_post.save()

        new_post.publish()
        return redirect('post_list')

    return render(request, 'blog/post_create.html', {})

class UserCreate(generic.CreateView):
#class UserCreate(UserCreationForm):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        messages.success(self.request, '帳戶已創立')
        return reverse('login')

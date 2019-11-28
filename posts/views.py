from django.shortcuts import render,redirect
from posts.models import Posts, PostsForm
def index(request):
    # return render(request,'index.html')
    form = PostsForm()
    data = Posts.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view/')

    return render(request,'index.html',{'title':'Add New Post','form':form,'rows':data})

def view(request):
    data = Posts.objects.all()
    # for mine in data:
    #     print(mine)
    return render(request,'view.html',{'rows':data})
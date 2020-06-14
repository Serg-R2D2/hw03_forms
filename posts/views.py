from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Group

from .forms import PostForm



def index(request):
    """Возвращает одиннадцать новых постов"""
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    """Возвращает двенадцать последних постов указанной темы"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request): 
    """Сохраняет новый пост после валидации формы"""
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form': form})
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})

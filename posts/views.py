from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import reverse, render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post, Group


def index(request):
    """Возвращает десять новых постов на каждой странице"""
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(
            request,
            'index.html',
            {'page': page, 'paginator': paginator}
            )


def group_posts(request, slug):
    """Возвращает десять последних постов указанной темы на каждой странице"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 
        "group.html", 
        {'page': page, 'paginator': paginator}
        )


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


def profile(request, username):
    """Вывод профайла пользователя социальной сети"""
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    paginator = Paginator(posts, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(
        request,
        'profile.html', 
        {'page': page,
        'paginator': paginator,
        'author': author}
        )
 
 
def post_view(request, username, post_id):
    """Вывод конкретного поста пользователя социальной сети"""
    author = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, id=post_id)
    post_num = Post.objects.filter(author=author).count()
    return render(
        request, 
        'post.html', 
        {'post':post,
        'author': author,
        'post_num': post_num}
        )


@login_required
def post_edit(request, username, post_id):
    """Редактирование поста"""
    post = get_object_or_404(
        Post, 
        author__username=username, 
        id=post_id
        )
    if post.author != request.user:
        post_url = reverse(
            'post', 
            args=(post.author, post.id)
            )
        return redirect(post_url)
    form = PostForm(instance=post)
    if request.method == 'POST':
        if form.is_valid():
            post.save()
            post_url = reverse(
                'post', 
                args=(post.author, post.id)
                )
            return redirect(post_url)   
    return render(
        request, 
        'new_post.html', 
        {'form': form, 'is_edit': True}
        )
# тут тело функции. Не забудьте проверить, 
# что текущий пользователь — это автор записи.
# В качестве шаблона страницы редактирования укажите шаблон создания новой записи
# который вы создали раньше (вы могли назвать шаблон иначе)


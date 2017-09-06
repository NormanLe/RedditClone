from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Post, Subblueit, Comment, UserProfile
from .forms import PostForm, SignUpForm, CommentForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.filter(karma__gte=0).order_by('-karma', '-pub_date')
    context = {'posts' : posts}
    u = UserProfile.objects.get(user__exact=request.user)
    context['subs'] = u.subs.all()
    return render(request, 'RedditApp/index.html', context)

def index_ordered(request, sorting):
    if sorting == 'hot':
        posts = Post.objects.filter(karma__gte=0).order_by('-karma', '-pub_date')
    elif sorting == 'new':
        posts = Post.objects.order_by('-pub_date')
    elif sorting == 'top':
        posts = Post.objects.filter(karma__gte=0).order_by('-karma')
    context = {'posts' : posts}
    u = UserProfile.objects.get(user__exact=request.user)
    context['subs'] = u.subs.all()
    return render(request, 'RedditApp/index.html', context)

def subblueit(request, subblueit_name):
    sub = get_object_or_404(Subblueit, name = subblueit_name)
    if (request.POST.get('subscribeButton')):
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.subs.add(sub)
    posts = sub.post_set.filter(
        pub_date__gte=timezone.now()-timezone.timedelta(days=7)).order_by('-karma')
    context = {'sub' : sub, 'posts' : posts}
    u = UserProfile.objects.get(user__exact=request.user)
    context['subs'] = u.subs.all()
    return render(request, 'RedditApp/sub.html', context)

def subblueit_ordered(request, subblueit_name, sorting):
    sub = get_object_or_404(Subblueit, name = subblueit_name)
    if (request.POST.get('subscribeButton')):
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.subs.add(sub)
    context = {'sub' : sub}
    sorting = sorting.lower()
    if sorting == 'hot':
        posts = sub.post_set.filter(karma__gte=0).order_by('-karma', '-pub_date')
    elif sorting == 'new':
        posts = sub.post_set.order_by('-pub_date')
    elif sorting == 'top':
        posts = sub.post_set.filter(karma__gte=0).order_by('-karma')
    context['posts'] = posts
    u = UserProfile.objects.get(user__exact=request.user)
    context['subs'] = u.subs.all()
    return render(request, 'RedditApp/sub.html', context)
def comments(request, subblueit_name, post_id, post_name):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.text = form.cleaned_data['comment']
            comment.pub_date = timezone.now()
            comment.karma = 0
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(
                reverse('RedditApp:post_detail',
                    kwargs={'subblueit_name' : subblueit_name,
                            'post_id' : post_id,
                            'post_name' : post_name}))
    else:
        form = CommentForm()
    return render(request, 'RedditApp/comments.html',
        {'post' : post, 'form' : form})

@login_required
def submit(request, subblueit_name):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.karma = 0
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('RedditApp:subblueit_detail',
                kwargs={'subblueit_name' : subblueit_name}))
    else:
        form = PostForm()
    return render(request, 'RedditApp/submit.html',
        {'form': form, 'sub':subblueit_name})

def user(request, user):
    return render(request, 'RedditApp/user.html', {'user' : user})

def login(request):
    return render(request, 'RedditApp/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(request, username=username, password=password)
            login_user(request, user)
            profile = UserProfile(user = user)
            profile.save()
            return HttpResponseRedirect(reverse('RedditApp:index'))
    else:
        form = SignUpForm()
    return render(request, 'RedditApp/signup.html', {'form': form})

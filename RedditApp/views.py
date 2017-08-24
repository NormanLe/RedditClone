from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Post, Subblueit
from .forms import PostForm

# Create your views here.
def index(request):
    popular_posts = Post.objects.order_by('-karma', '-pub_date')
    context = {
        'popular_posts' : popular_posts
    }
    # method to call, depending on sorting, that returns the context, given a sub and a desired sort
    return render(request, 'RedditApp/index.html', context)

def subblueit(request, subblueit_name, sorting):
    
    sub = get_object_or_404(Subblueit, name = subblueit_name)
#    if sorting == hot: context = {}
#    else: it's just normal viewing
    return render(request, 'RedditApp/sub.html', {'sub' : sub})

def comments(request, subblueit_name, post_id, post_name):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'RedditApp/comments.html', {'post' : post})

def submit(request, subblueit_name):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.karma = 0
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('RedditApp:subblueit_detail', kwargs={'subblueit_name' : subblueit_name}))
    else:
        form = PostForm()
    return render(request, 'RedditApp/submit.html', {'form': form, 'sub':subblueit_name})

def user(request, user):
    return render(request, 'RedditApp/user.html', {'user' : user})

def login(request):
    return render(request, 'RedditApp/login.html')

def apply_sorting_choice(choice, sub):
    pass
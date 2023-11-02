from django.shortcuts import render, redirect
from .forms import BlogFrom, WordForm
from .models import Topic, Blog, Author, Word, Comment, Client, WordCollection
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully') 
        return redirect('login')
    context = {'form':form}
    return render(request, 'base/register.html', context)
        


def home(request):
    author = Author.objects.filter(user__id=request.user.id)
    client = Client.objects.filter(user__id=request.user.id)
    recent_blogs = Blog.objects.order_by("-id")[0:5]
    popular_blogs = Blog.objects.order_by("-views")[0:5]
    check_client = 0
    check_author = 0
    if author.exists():
        check_author = 1
        check_client = 1
    if client.exists():
        check_client = 1
    q = request.GET.get("search") if request.GET.get("search") is not None else ''
    blogs = Blog.objects.filter(
        Q(topic__name__icontains = q) |
        Q(author__user__first_name__icontains = q) |
        Q(author__user__last_name__icontains = q) |
        Q(title__icontains = q)     
    )
    topics = Topic.objects.all()
    context = {'blogs':blogs, 'topics':topics, 'check_author':check_author, 'check_client':check_client
        , 'recent_blogs':recent_blogs, 'popular_blogs':popular_blogs}
    return render(request, 'base/home.html', context)


def authorPage(request, pk):
    author = Author.objects.get(id=pk)
    context = {'author':author}
    return render(request, 'base/author.html', context)


@login_required(login_url="/login")
def createBlog(request):
    author = Author.objects.get(user__id = request.user.id)
    form = BlogFrom()
    if request.method == 'POST':
        form = BlogFrom(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.content = request.POST["content"]
            blog.author = author
            blog.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/create_blog.html', context)


@login_required(login_url="/login")
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogFrom(instance=blog)
    if request.method == 'POST':
        form = BlogFrom(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.content = request.POST["content"]
            blog.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/create_blog.html', context)


def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.views += 1
    blog.save()
    comments = Comment.objects.filter(blog__id=pk)
    try:
        author = Author.objects.get(user__id=request.user.id)
    except Author.DoesNotExist:
        author = None
    try:
        client = Client.objects.get(user__id=request.user.id)
    except Client.DoesNotExist:
        client = None
        
    words = Word.objects.filter(blog__id=pk)
    q = request.GET.get('word') 
    formWord = WordForm()
    word_search = Word()
    if request.GET.get('word') is not None:
        try:
            word_search = Word.objects.get(word=q)
        except word_search.DoesNotExist:
            word_search = None
            messages.error(request, 'Word is not exist!') 
        if word_search is not None:
            formWord = WordForm(instance=word_search)  
    else:
        word_search = None    
    
    recent_blogs = Blog.objects.order_by("-id")[0:5]
    popular_blogs = Blog.objects.order_by("-views")[0:5]
    check_author = 0
    check_client = 0
    new_word = WordCollection()
    comment = Comment()
    if client is not None or author is not None:
        check_client = 1
        if request.method == 'POST':
            if request.POST.get('word_study') is not None:
                new_word.word = Word.objects.get(id=request.POST["word_study"]) 
                new_word.user = request.user
                new_word.save()
            if request.POST.get("comment") is not None:
                comment.user = request.user
                comment.content = request.POST["comment"]
                comment.blog = blog
                comment.save()
            formWord = WordForm(request.POST, instance=word_search)
            if formWord.is_valid():
                word_add = formWord.save()
                word_add.blog.add(blog)
                word_add.save()
                print("ok")
                return redirect('blog',blog.id)
            return redirect('blog',blog.id)
    
    if author is not None:
        check_author = 1
    context = {'blog':blog, 'check_author':check_author, 'recent_blogs':recent_blogs, 'check_client':check_client,
               'popular_blogs':popular_blogs, 'word_search':word_search, 'words':words, 'formWord':formWord, 'comments':comments}
    return render(request, 'base/blog.html', context)


def createWord(request, pk):
    blog = Blog.objects.get(id=pk)
    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES)
        if form.is_valid():
            word = form.save()
            word.blog.add(blog)
            word.save()
            return redirect('blog',blog.id)
    context = {'form':form}
    return render(request, 'base/create_word.html', context)


def myVocabs(request):
    recent_blogs = Blog.objects.order_by("-id")[0:5]
    popular_blogs = Blog.objects.order_by("-views")[0:5]
    words = WordCollection.objects.filter(user__id=request.user.id)
    all_count = len(words)
    easy_words = WordCollection.objects.filter(user__id=request.user.id, level="Easy")
    medium_words = WordCollection.objects.filter(user__id=request.user.id, level="Medium")
    hard_words = WordCollection.objects.filter(user__id=request.user.id, level="Hard")
    try:
        author = Author.objects.get(user__id=request.user.id)
    except Author.DoesNotExist:
        author = None
    try:
        client = Client.objects.get(user__id=request.user.id)
    except Client.DoesNotExist:
        client = None
    if client is not None or author is not None:
        check_client = 1
    q = request.GET.get('level')
    if q is not None:
        if q == "easy":
            words = easy_words
        elif q == "medium":   
            words = medium_words
        else:
            words = hard_words
    if request.method == 'POST':
        for word in words:
            id = str(word.word.id)
            if request.POST.get(id) ==  "0":
                word.level = "Easy"
            elif request.POST.get(id) == "1":
                word.level = "Medium"
            else:
                word.level = "Hard"
            word.save()
    
    context = {'words':words, 'check_client':check_client, 'easy_words':easy_words, 'medium_words':medium_words,
        'hard_words':hard_words, 'all_count':all_count, 'recent_blogs':recent_blogs, 'popular_blogs':popular_blogs}
    return render(request, 'base/my_vocabs.html', context)
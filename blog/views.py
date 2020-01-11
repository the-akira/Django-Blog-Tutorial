from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post
from operator import attrgetter
from django.db.models import Q

class PostListView(ListView):
	model = Post 
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	ordering = ['-data']
	paginate_by = 4

class PostDetailView(DetailView):
	model = Post

def get_post_queryset(query=None):
    queryset = []
    queries = query.split(' ') # python install 2019 = ['python', 'install', '2019']
    for q in queries:
        posts = Post.objects.filter(Q(titulo__icontains=q)| Q(conteudo__icontains=q) ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

def search(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    posts = sorted(get_post_queryset(query), key=attrgetter('titulo'), reverse=True)
    context['posts'] = posts
    return render(request, 'blog/search.html', context)
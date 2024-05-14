from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404, HttpResponse

def post_list(request):
    posts = Post.objects.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # try:
    #     post = (Post.publish.get(id=pk))
    # except Post.DoesNotExist:
    #     raise Http404('Post does not exist')
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

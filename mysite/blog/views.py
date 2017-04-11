from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.

def post_list(request):

    #posts = Post.objects.filter(status='published')
    object_list = Post.published.all()
    paginator = Paginator(object_list,2)
    page = request.GET.get('page',1)
    print(page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request,'blog/post/list.html',{'page':page,'posts':posts})

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,'blog/post/detail.html',{'post':post})

def post_share(request,post_id):
    #retrieve post by id
    #post = Post.objects.get(id=post_id,status='published')
    post = get_object_or_404(Post,id=post_id,status='published')
    sent = False
    print(post.get_absolute_url())
    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = post.get_absolute_url()
            print (post_url)
            subject = '%s %s recommends you reading "%s"' %(cd['name'],cd['email'],post.title)
            print (subject)
            message = 'Read "%s" at %s \n\n%s\'s comments: %s' %(post.title,post_url,cd['name'],cd['comments'])
            print (message)
            send_mail(subject,message,from_email='2388992177@qq.com',recipient_list=[cd['to']])
            sent = True
    else:
        form=EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})
'''
class PostListView(ListView):

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
'''
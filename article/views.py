from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm,EmailPostForm
from django.contrib.auth.decorators import login_required
from public.paginate_queryset import paginate_queryset
from comment.models import Comment


def article_list(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	article_objs = Article.objects.filter(block=block,status=0).order_by('-id')
	return render(request,'article_list.html',{'articles':article_objs,'b':block})

@login_required
def article_create(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	owner = request.user

	if request.method == "GET":
		return render(request,'article_create.html',{'b':block})
	else:
		'''
		title = request.POST['title'].strip()
		content = request.POST['content'].strip()
		#标题与内容为空异常处理
		if not title or not content:
			return render(request,'article_create.html',{'b':block,'error':'标题和内容都不能为空',"title":title,"content":content})
		#标题与内容长度异常处理
		if len(title) > 100 or len(content) > 10000:
			return render(request,'article_create.html',{'b':block,'error':'标题或内容太长了',"title":title,"content":content})
		'''
		form = ArticleForm(request.POST)
		if form.is_valid():
			'''
			article = Article(block=block,title=form.cleaned_data['title'],content=form.cleaned_data['content'],status=0)
			article.save()
			'''
			article = form.save(commit=False)
			article.block = block
			article.owner = owner
			article.status = 0
			article.save()
			return redirect("/article/list/%s" %block_id)
		else:
			return render(request,"article_create.html",{'b':block,'form':form})

def article_detail(request,article_id):
	article_id = int(article_id)
	article = Article.objects.get(id=article_id)
	all_comments = Comment.objects.filter(article=article_id,status=0).order_by('-id')
	page_no = int(request.GET.get("page_no",1))
	page_comments,pagination_data = paginate_queryset(all_comments,page_no,cnt_per_page=3,half_show_length=3)
	return render(request,'article_detail.html',{'comments':page_comments,'a':article,
					'pagination_data':pagination_data})



def listing(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	ARTICLE_CNT_1PAGE = 1
	all_articles = Article.objects.filter(block=block,status=0).order_by('-id')
	page_no = int(request.GET.get("page_no",1))
	page_articles,pagination_data = paginate_queryset(all_articles,page_no,cnt_per_page=1,half_show_length=3)
	return render(request,'article_list.html',{'articles':page_articles,'b':block,
					'pagination_data':pagination_data})

def article_share(request,article_id):
	article_id = int(post_id)
	article = Article.objects.get(id=article_id)
	if request == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#send email
	else:
		form = EmailPostForm()
	return render(request,'article_share.html',{'post':post,'form':form})


	

	#start_index = (page_no-1) * ARTICLE_CNT_1PAGE
	#end_index =page_no * ARTICLE_CNT_1PAGE
	#contacts = Article.objects.filter(block=block,status=0).order_by('-id')[start_index:end_index]
	'''
	p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
	page_no = int(request.GET.get("page_no",1))
	print (page_no)
	try:
		contacts = p.page(page_no)
	except PageNotAnInteger:
		#if page_no is not a integer ,deliver first page
		contacts = p.page('1')
	except EmptyPage:
		contacts = p.page(p.num_pages)
	'''
	'''
	return render(request,'article_list.html',{'articles':article_objs,'b':block,
		'page_cnt':page_cnt,'current_no':current_no,'page_links':page_links,
		'previous_link':'previous_link','next_link':next_link,'has_previous':has_previous,
		'has_next':has_next})
	'''

from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required

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
	return render(request,'article_detail.html',{'a':article})

def paginate_queryset(objs,page_no,cnt_per_page=10,half_show_length=5):
	p = Paginator(objs,cnt_per_page)
	if page_no > p.num_pages:
		page_no = p.num_pages
	if page_no <=0:
		page_no = 1
	page_links = [i for i in range(page_no - half_show_length,page_no + half_show_length+1)
	if i > 0 and i <= p.num_pages]
	page = p.page(page_no)
	previous_link = page_links[0] - 1
	next_link = page_links[-1] + 1
	pagination_data = {'has_previous':previous_link > 0,
						'has_next':next_link <= p.num_pages,
						'previous_link':previous_link,
						'next_link':next_link,
						'page_cnt':p.num_pages,
						'current_no':page_no,
						'page_links':page_links}
	return (page.object_list,pagination_data)

def listing(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	ARTICLE_CNT_1PAGE = 1
	all_articles = Article.objects.filter(block=block,status=0).order_by('-id')
	page_no = int(request.GET.get("page_no",1))
	page_articles,pagination_data = paginate_queryset(all_articles,page_no,cnt_per_page=1,half_show_length=3)
	return render(request,'article_list.html',{'articles':page_articles,'b':block,
					'pagination_data':pagination_data})
	

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

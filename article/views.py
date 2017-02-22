from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator

def article_list(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	article_objs = Article.objects.filter(block=block,status=0).order_by('-id')
	return render(request,'article_list.html',{'articles':article_objs,'b':block})

def article_create(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)

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
			article.status = 0
			article.save()
			return redirect("/article/list/%s" %block_id)
		else:
			return render(request,"article_create.html",{'b':block,'form':form})

def article_detail(request,article_id):
	article_id = int(article_id)
	article = Article.objects.get(id=article_id)
	return render(request,'article_detail.html',{'a':article})

def listing(request):
	page_no = int(request.GET.get("page_no","1"))
	ARTICLE_CNT_1PAGE = 1
	all_articles = Article.objects.filter(block=block,status=0)
	p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
	page = p.page(page_no)
	article_objs = page.object_list
	print (article_objs)
	print ('=====')

	return render(request,'article_list.html',{'articles':article_objs})
from .models import Comment
from article.models import Article
from django.shortcuts import render
import json
def json_response(obj):
	txt = json.dumps(obj)
	return txt

def create_comment(request,article_id):
	
	owner = request.user
	article_id = int(article_id)
	article = Article.objects.get(id=article_id)
	comment = request.POST['comment'].strip()
	if not comment:
		return render(request,'article_detail.html',{'a':article,'error':'评论内容不能为空'})
		json_response({'status':'err','msg':'评论内容不能为空'})

	comment = Comment(owner=owner,article=article,comment=comment,status=0)
	comment.save()
	json_response({'status':'ok','msg':''})
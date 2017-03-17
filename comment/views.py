from .models import Comment
from article.models import Article
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from message.models import Message

@login_required
def create_comment(request):

    owner = request.user

    if request.method == 'POST':
        article_id = int(request.POST["article_id"])
        article = Article.objects.get(id=article_id)
        content = request.POST["content"].strip()
        to_comment_id = int(request.POST.get('to_comment_id',0))

        if to_comment_id != 0:
            to_comment = Comment.objects.get(id=to_comment_id)
            if content:
                comment = Comment(owner=owner, content=content, article=article, to_comment=to_comment, status=0)
                comment.save()
                recevier = to_comment.owner
                print (recevier)
                print (to_comment.content)
                print (to_comment.owner)
                link = '/article/detail/'+(str(article_id))
                msg_content = "%s回复了你的评论%s" %(owner,to_comment.content)
                message = Message(owner=recevier,content=msg_content,link=link,status=0)
                message.save()
                success_ret = json.dumps({'status': 'ok', 'msg': 'success'})
                return HttpResponse(success_ret)
            else:
                failure_ret = json.dumps({'status': 'error', 'msg': 'content is empty'})
                return HttpResponse(failure_ret)
        else:
            to_comment = None
            if content:
                comment = Comment(owner=owner, content=content, article=article, to_comment=to_comment, status=0)
                comment.save()
                recevier = owner
                print(recevier)
                link = '/article/detail/' + (str(article_id))
                print(link)
                msg_content = "%s评论了您的文章%s" %(owner,article.title)
                message = Message(owner=recevier,content=msg_content,link=link,status=0)
                message.save()
                success_ret = json.dumps({'status': 'ok', 'msg': 'success'})
                return HttpResponse(success_ret)
            else:
                failure_ret = json.dumps({'status': 'error', 'msg': 'content is empty'})
                return HttpResponse(failure_ret)
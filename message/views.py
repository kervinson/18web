from django.shortcuts import render,redirect
from .models import Message
from public.paginate_queryset import paginate_queryset

def message_list(request):
    owner = request.user
    print (owner)
    all_unread_messages = Message.objects.filter(owner=owner,status=0).order_by('-id')
    #msg_cnt = Message.objects.filter(owner,status=0).count()
    page_no = int(request.GET.get('page_no',1))
    page_messages,pagination_data = paginate_queryset(all_unread_messages,page_no,cnt_per_page=3,half_show_length=3)

    return render(request,'message_list.html',{'unread_messages':page_messages,'pagination_data':pagination_data})

def read_message(request,msg_id):

    message_id = int(msg_id)
    print(message_id)
    message = Message.objects.get(id=message_id)
    print(message.link)
    #message.status = -1
    #message.save()
    return  redirect(message.link)
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Member
from .form import MemberForm

# Create your views here.
def home(request):
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=MemberForm()

    #return HttpResponse("This is home page❤️")
    all_members=Member.objects.all()
    return render(request,'home.html',{'form':form,'all':all_members})
def about(request):
    return HttpResponse("This is about page😁")
def contact(request):
    #return HttpResponse("This is contact page🤔")
    return render(request,'contact.html')
def update_member(request,id):
    member=get_object_or_404(Member,id=id)

    if request.method=='POST':
        form=MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=MemberForm(instance=member)
    return render(request,'update.html',{'form':form})
def delete_member(request,id):
    member=get_object_or_404(Member,id=id)
    member.delete()
    return redirect('home')
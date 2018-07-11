from django.shortcuts import render ,get_object_or_404 , HttpResponse ,redirect
from .models import Poll , Question ,Vote
from . form import form_poll_add ,form_poll_edit ,form_add_choice
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages

# Create your views here.


def poll_list(request):
    poll = Poll.objects.all()
    if 'text' in request.GET:
        poll = poll.order_by('text')
    if 'timestamp' in request.GET:
        poll = poll.order_by('timestamp')
    context = {
        "poll":poll
    }
    template_name="poll_list.html"
    return render(request,template_name,context)


def home(requset):
    template_name = "home.html"
    return render(requset,template_name)


def poll_signle(request,id):
    instance = get_object_or_404(Poll,id=id)

    context = {

        "instance":instance
    }
    template_name = "poll_single.html"
    return render(request,template_name,context)

@login_required
def poll_vote(request,id):
    poll = get_object_or_404(Poll,id=id)
    if not poll.user_can_vote(request.user):
        return redirect("polls:home")
    # we used get method because we know POST is dictionary and key is Choice so
    # that's why we use .get method
    # other wise we have to use  ==>> choice_id = request.POST['choice']
    choice_id = request.POST.get('choice',None)
    if choice_id:
        choice = Question.objects.get(id=choice_id)
        new_vote = Vote(user=request.user,poll=poll,question=choice)
        new_vote.save()
    context = {"error":True}
    template_name ="poll_vote.html"
    return render (request , template_name , context)




@login_required
def poll_add(requset):
    if requset.method == "POST":
        form = form_poll_add(requset.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.timestamp = datetime.datetime.now()
            new_form.owner = requset.user
            new_form.save()
            print(form.cleaned_data)
            new_choice = Question (poll = new_form,
            choice_text = form.cleaned_data["choice1"] ).save()
            new_choice2 = Question(poll=new_form,
                                  choice_text=form.cleaned_data["choice2"]).save()
            messages.success(requset,"Poll and Choices added")
            return redirect("polls:home")
    else :
        form = form_poll_add()
    template_name= "poll_add.html"
    return render(requset,template_name,{'form':form})





def contact(request):
    return render(request,"contact.html",locals())


@login_required
def edit(request,id):
    poll = get_object_or_404(Poll,id=id)
    if request.method == "POST" :
        form = form_poll_edit(request.POST,instance=poll)
        if form.is_valid():
            form.save()
            messages.success(request,"Edit success!")
            return redirect("polls:home")

    else :
        form = form_poll_edit(instance=poll)
    context = {'poll': poll,
               "form":form}
    template_name = 'edit.html'
    return render(request,template_name,context)



def add_choice(request,id):
    poll = get_object_or_404(Poll,id=id)
    if request.method == "POST":
        form = form_add_choice(request.POST)
        if form.is_valid():
            new_choice =form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            return redirect("polls:home")
    else:
        form = form_add_choice()

    return render(request,template_name="add_choice.html",context= {"poll":poll,"form":form})




def edit_choice(request,id):
    choice = get_object_or_404(Question,id=id)
    poll = get_object_or_404(Poll,id=choice.poll.id)
    if request.method == "POST":
        form = form_add_choice(request.POST,instance=choice)
        if form.is_valid():
            form.save()
            return redirect("polls:home")
    else:
        form = form_add_choice()

    return render(request,template_name="edit_choice.html",context={"poll":poll,"form":form, "choice":choice , "edit_mode":True})



def delete_choice(request,id):
    choice = get_object_or_404(Question,id=id)
    poll = get_object_or_404(Poll,id=choice.poll.id)
    if request.method == "POST":
        choice.delete()
        return redirect("polls:polls_list")


    return render(request,template_name="delete_choice.html",context={"poll":poll,"choice":choice})




def delete_poll(request,id):
    poll = get_object_or_404(Poll,id=id)
    if request.method == "POST":
        poll.delete()
        return redirect('polls:home')

    return render(request,template_name="delete_poll.html",context={"poll":poll})


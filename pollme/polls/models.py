from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Poll(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add=False,auto_now = True)


    def __str__(self):
        return self.text



    def user_can_vote(self,user):
        user_vote = user.vote_set.all()
        qs = user_vote.filter(poll=self)
        if qs.exists():
            return False
        else:
            return True




    @property
    def vote_num(self):
        return self.vote_num.count()





class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)



    class Meta :
        ordering = ["poll"]

    def __str__(self):
        return "{}-{}".format(self.poll.text[:25],self.choice_text[:25])

    @property
    def num_votes(self):
        return self.vote_set.count()


class Vote (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)



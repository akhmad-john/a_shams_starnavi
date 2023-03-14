from django.db import models
from core.models import TimeStampMixin
from account.models import User


class Post(TimeStampMixin):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def likes(self):
        return Like.objects.filter(post_id=self.id).count()


class Like(TimeStampMixin):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post_id', 'user_id')

    def __str__(self):
        return "{} - {}".format(self.post_id.title, self.user_id.username)

from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='friend_name'
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='block_name',
    )

    def __str__(self):
        return self.name

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def posts(self):
        return self.post_set.all()


class UserInfo(models.Model):
    name = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def like_users(self):
        return [i.user for i in self.postlike_set.all()]

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def like_user(self):
        return [i.user for i in self.commentlike_set.all()]

    def __str__(self):
        # return self.user.name
        return str(self.user)
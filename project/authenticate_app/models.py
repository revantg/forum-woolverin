from django.db import models

class thread(models.Model):
    TOPIC_CHOICES = (
        ('TOPIC1', (
            ('S1', 'Subtopic 1'),
            ('S2', 'Subtopic 2 (Default)'),
        )
        ),
        ('TOPIC2', (
            ('S3', 'Subtopic 3'),
            ('S3', 'Subtopic 4'),
        )
        ),
        ('OT', 'OTHER'),
    )
    user_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, unique=True)
    topic = models.CharField(
        max_length=2, choices=TOPIC_CHOICES, default="Subtopic 2")
    datetime = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length = 150)
    post_body = models.TextField()  
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.subject


class reply(models.Model):
    parent_post = models.ForeignKey('thread', on_delete=models.CASCADE)
    # parent_id = models.ForeignKey('thread', on_delete = "CASCADE")
    user_name = models.CharField(max_length=50, default = "Anonymous")
    date_field = models.DateTimeField(auto_now=True)
    reply_body = models.TextField(null = False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.reply_body[:20] + "....."

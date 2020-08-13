from django.db import models


# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    blog_author = models.CharField(max_length=20, default="Anonymous")
    blog_title = models.CharField(max_length=50, default="Blog Title")
    post_date = models.DateField(auto_now=True)
    blog_main = models.CharField(max_length=500, default="")
    head0 = models.CharField(max_length=50, default="")
    head0_content = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=50, default="")
    head1_content = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=50, default="")
    head2_content = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.blog_title

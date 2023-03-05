from django.db import models


# Create your models here.
class webdb(models.Model):
    name = models.CharField(max_length=45, unique=True, help_text="網站名稱")
    url = models.URLField(max_length=200, help_text="網站位置")
    exist = models.BooleanField(default=True, help_text="是否啟用")

    def __str__(self):
        return "[{}]".format(self.name)

    class Meta:
        ordering = ['id']
        db_table = "web"

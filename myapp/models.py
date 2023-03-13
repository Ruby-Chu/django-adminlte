from django.db import models


# Create your models here.
class FIRST_MENU(models.Model):
    first = models.CharField(max_length=45, unique=True, help_text="主選單名稱")
    url = models.CharField(max_length=200, default="#", help_text="網站位置")
    exist = models.BooleanField(default=True, help_text="是否啟用")

    def __str__(self):
        return "[{}]".format(self.first)

    class Meta:
        ordering = ['id']
        db_table = "first_menu"
        verbose_name_plural = "主選單"


class SECOND_MENU(models.Model):
    second = models.CharField(max_length=45, unique=True, help_text="次選單名稱")
    first_menu = models.ForeignKey(FIRST_MENU, on_delete=models.DO_NOTHING, db_column="first_menu_id")
    url = models.CharField(max_length=200, default="#", help_text="網站位置")
    exist = models.BooleanField(default=True, help_text="是否啟用")

    def __str__(self):
        return "[{}]".format(self.second)

    class Meta:
        ordering = ['id']
        db_table = "second_menu"
        verbose_name_plural = "次選單"
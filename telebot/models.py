from django.db import models

# Create your models here.
class SettingTg(models.Model):
    st_token = models.CharField(max_length=200,verbose_name="Токен бота")
    st_id_group = models.CharField(max_length=200, verbose_name="ID Группы")
    st_text = models.TextField(verbose_name="Текст сообщения")
    def __str__(self):
        return self.st_text

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

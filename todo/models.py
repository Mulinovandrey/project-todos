from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100) #создание модели заголовка
    memo = models.TextField(blank=True) #создание модели описания, blank=True делает это поле необязательным для заполнения
    created = models.DateTimeField(auto_now_add=True) #создание модели времени поста, auto_now_add=True автоматически добавляет время поста
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False) # создание модели важности задачи, defaul=False определяет необязательность проставления важности задачи
    user = models.ForeignKey(User, on_delete=models.CASCADE) # для определения связи между записью и пользователем, оно осуществляется благодаря уникальному ID у каждого пользователя

    def __str__(self):
        return self.title # функция необходимая для отображения названия заметки в панели админа

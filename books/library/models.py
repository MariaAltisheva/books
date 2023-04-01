from django.db import models



class BaseModel(models.Model):
    create_data = models.DateField(verbose_name='дата добавления читателя', auto_now=True)
    edit_data = models.DateField(verbose_name='дата редактирования читателя', auto_now_add=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    first_name = models.CharField(verbose_name='имя автора', max_length=50)
    last_name = models.CharField(verbose_name='фамилия автора', max_length=50)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        unique_together = ('first_name', 'last_name')
        # permissions = ('can_some_rules', 'Can some rules')

class Book(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    total_page = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Reader(BaseModel):
    class Status(models.TextChoices):
        is_active = 'активен'
        not_active = 'не активен'


    first_name = models.CharField(verbose_name='имя читателя', max_length=100)
    last_name = models.CharField(verbose_name='фамилия читателя', max_length=100)
    phone_number = models.CharField(verbose_name='телефон читателя', max_length=20, null=True, blank=False)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.is_active)
    active_books = models.ManyToManyField(Book,max_length=3)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    # связь с правами доступа, используем свойство related_name, чтобы избежать конфликтов
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'




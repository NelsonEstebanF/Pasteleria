from django.db.models import Model, CharField, TextField, DateTimeField, ImageField

class Postre(Model):
    title = CharField(max_length=50, verbose_name='Título')
    description = TextField(verbose_name='Descripción')
    image = ImageField(upload_to='Postre')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Postre'
        verbose_name_plural = 'Postres'

    def __str__(self) -> str:
        return self.title
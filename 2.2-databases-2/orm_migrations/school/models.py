from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return f'{self.name}   {self.subject}'


class Student(models.Model):
    name = models.CharField(max_length=100, default='Александр Александров', verbose_name='Имя')
    group = models.CharField(max_length=100, default='4-А', verbose_name='Класс')
    teacher = models.ManyToManyField(Teacher, related_name='students')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return f'{self.name}'


class StudentPosition(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='position')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='position')

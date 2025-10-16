from django.db import models


class Document(models.Model):
    series = models.CharField(max_length=20, verbose_name="Серия")
    number = models.CharField(max_length=20, verbose_name="Номер")
    issue_date = models.DateField(verbose_name="Дата выдачи")
    issued_by = models.CharField(max_length=255, verbose_name="Кем выдан")

    def __str__(self):
        return f"{self.series} {self.number}"


class Guest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    birth_date = models.DateField(verbose_name="Дата рождения")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name="Документ")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Скидка")


    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Room(models.Model):
    floor = models.IntegerField(verbose_name="Этаж")
    room_count = models.IntegerField(verbose_name="Количество комнат")
    bed_count = models.IntegerField(verbose_name="Количество спальных мест")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.floor


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name


class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Предмет")

    def __str__(self):
        return f"{self.category.name} - {self.item.name}"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, verbose_name="Клиент")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Номер")
    check_in_date = models.DateField(verbose_name="Дата заезда")
    check_out_date = models.DateField(verbose_name="Дата выезда")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="ОплаченоФакт")

    def __str__(self):
        return f"Бронирование {self.id} - {self.guest.full_name}"


class ServiceProvision(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name="Бронирование")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    service_date = models.DateField(verbose_name="Дата оказания услуги")

    def __str__(self):
        return f"{self.service.name} - {self.booking}"
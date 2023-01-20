from django.db import models


class Posada(models.Model):
    posad_name = models.CharField(max_length=100)
    posad_cod = models.CharField(max_length=20)

    def __str__(self):
        return self.posad_name


class Zvannya(models.Model):
    zvannya_name = models.CharField(max_length=100)
    zvannya_is_officer = models.BooleanField()
    zvannya_is_sergeant = models.BooleanField()
    zvannya_is_soldier = models.BooleanField()

    def __str__(self):
        return self.zvannya_name


class Object(models.Model):
    object_name = models.CharField(max_length=50)
    object_code = models.CharField(max_length=50)

    def __str__(self):
        return str(self.object_name) + "(" + str(self.object_code) + ")"


class Rota(models.Model):
    rota_number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rota_number)


class Vzvod(models.Model):
    vzvod_name = models.CharField(max_length=30)

    def __str__(self):
        return self.vzvod_name


class Soldier(models.Model):
    soldier_name = models.CharField(max_length=150)
    soldier_birthd = models.DateField()
    soldier_osvita = models.CharField(max_length=200)
    soldier_rvk = models.CharField(max_length=200)
    soldier_stan_adres = models.CharField(max_length=250)
    soldier_fin_id = models.IntegerField()
    soldier_zvannya = models.ForeignKey(Zvannya, on_delete=models.PROTECT)

    def __str__(self):
        return self.soldier_name


class Shtat(models.Model):
    posad_nomer = models.IntegerField(verbose_name="Номер посади")
    zv_shtat = models.ForeignKey(Zvannya, verbose_name="Звання штат", on_delete=models.PROTECT)
    date_priznach = models.DateField(verbose_name="Дата призначення")

    object = models.ForeignKey(Object, verbose_name="Об'єкт", on_delete=models.PROTECT, related_name="object", default=None)
    objectfact = models.ForeignKey(Object, verbose_name="Об'єкт факт", on_delete=models.PROTECT, related_name="objectfact", default=None)

    rota = models.ForeignKey(Rota, verbose_name="Рота", on_delete=models.PROTECT)
    vzvod = models.ForeignKey(Vzvod, verbose_name="Взвод", on_delete=models.PROTECT)
    soldier = models.ForeignKey(Soldier, verbose_name="ПІБ", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.posad_nomer) + " " + str(self.soldier)

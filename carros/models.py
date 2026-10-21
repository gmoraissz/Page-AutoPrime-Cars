from django.db import models
from django.urls import reverse


class Carro(models.Model):
    class Combustivel(models.TextChoices):
        FLEX = "flex", "Flex"
        GASOLINA = "gasolina", "Gasolina"
        DIESEL = "diesel", "Diesel"
        ELETRICO = "eletrico", "Elétrico"
        HIBRIDO = "hibrido", "Híbrido"

    class Cambio(models.TextChoices):
        MANUAL = "manual", "Manual"
        AUTOMATICO = "automatico", "Automático"

    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=80)
    versao = models.CharField("versão", max_length=100, blank=True)
    ano = models.PositiveSmallIntegerField()
    quilometragem = models.PositiveIntegerField(default=0)
    preco = models.DecimalField("preço", max_digits=10, decimal_places=2)
    combustivel = models.CharField(
        "combustível", max_length=10, choices=Combustivel.choices, default=Combustivel.FLEX
    )
    cambio = models.CharField(
        "câmbio", max_length=10, choices=Cambio.choices, default=Cambio.MANUAL
    )
    cor = models.CharField(max_length=40, blank=True)
    descricao = models.TextField("descrição", blank=True)
    foto = models.ImageField(upload_to="carros/%Y/%m/", blank=True)
    destaque = models.BooleanField(default=False)
    disponivel = models.BooleanField("disponível", default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-destaque", "-criado_em"]
        verbose_name = "carro"
        verbose_name_plural = "carros"

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}"

    def get_absolute_url(self):
        return reverse("detalhe", kwargs={"pk": self.pk})


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField(blank=True)
    carro = models.ForeignKey(
        Carro, on_delete=models.SET_NULL, null=True, blank=True, related_name="contatos"
    )
    lido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.nome} ({self.criado_em:%d/%m/%Y})"

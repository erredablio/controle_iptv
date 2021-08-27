from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=True)
    celular = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'Clientes'

    def __str__(self):
        return self.nome    

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'Produtos'

    def __str__(self):
        return self.nome

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    prazo = models.IntegerField(null=False)
    data_compra = models.DateField()
    quantidade = models.IntegerField(default=1, null=False)
    preco_compra = models.FloatField(default=1, null=False)

    class Meta:
        db_table = 'Compras'

    def __str__(self):
        return self.produto.nome

class Licenca(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cartao = models.CharField(max_length=200, null=False)
    codigo = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'Licencas'

    def __str__(self):
        return self.compra.produto.nome

class Venda(models.Model):
    licenca = models.ForeignKey(Licenca, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()
    preco_venda = models.FloatField(default=1, null=False)

    class Meta:
        db_table = 'Vendas'

    def __str__(self):
        return self.cliente.nome
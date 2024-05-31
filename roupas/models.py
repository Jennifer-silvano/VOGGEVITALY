from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class Categoria(models.Model):
    FEMININO = 'F'
    MASCULINO = 'M'
    UNISSEX = 'U'
    
    GENERO_CHOICES = [
        (FEMININO, 'Feminino'),
        (MASCULINO, 'Masculino'),
        (UNISSEX, 'Unissex'),
    ]

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default=UNISSEX)

    def __str__(self):
        return f'{self.nome} ({self.get_genero_display()})'


class Marca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)  # URL para o logo da marca

    def __str__(self):
        return self.nome

class Produto(models.Model):
    FEMININO = 'F'
    MASCULINO = 'M'
    UNISSEX = 'U'
    
    GENERO_CHOICES = [
        (FEMININO, 'Feminino'),
        (MASCULINO, 'Masculino'),
        (UNISSEX, 'Unissex'),
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=5)
    cor = models.CharField(max_length=50)
    imagem_url = models.URLField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default=UNISSEX)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
     CLIENTE = 'cliente'
     ADMINISTRADOR = 'administrador'

     TIPO_CHOICES = [
        (CLIENTE, 'Cliente'),
        (ADMINISTRADOR, 'Administrador'),
    ]

     tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=CLIENTE)

     def __str__(self):
        return self.username

class Cliente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
       

    def __str__(self):
        return self.user.username
   
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pendente", "Pendente"),
            ("pago", "Pago"),
            ("enviado", "Enviado"),
            ("entregue", "Entregue"),
        ],
    )
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return f"Item {self.id} - {self.pedido.id}"


class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipo_pagamento = models.CharField(
        max_length=50,
        choices=[
            ("cartao_credito", "Cartão de Crédito"),
            ("boleto", "Boleto"),
            ("pix", "Pix"),
        ],
    )
    status_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("pendente", "Pendente"),
            ("aprovado", "Aprovado"),
            ("recusado", "Recusado"),
        ],
    )
    data_pagamento = models.DateTimeField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Pagamento {self.id} - {self.pedido.id}"


class AvaliacaoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Avaliação {self.id} - {self.produto.nome}"


class Endereco(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="enderecos"
    )
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Endereço {self.id} - {self.cliente.username}"


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrinho {self.id} - {self.cliente.username}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Item {self.id} - {self.carrinho.id}'

class Wishlist(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Wishlist {self.id} - {self.cliente.username}'

class ItemWishlist(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Item {self.id} - Wishlist {self.wishlist.id}'


from django.db import models

class EnderecoEntrega(models.Model):
    # Defina os campos necessários para o endereço de entrega
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    # Adicione outros campos conforme necessário

    def __str__(self):
        return f'{self.rua}, {self.cidade}, {self.estado}, {self.cep}'


class CupomDesconto(models.Model):
    codigo = models.CharField(max_length=50)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    # outros campos necessários para o cupom de desconto

    def __str__(self):
        return self.codigo
    

class HistoricoCompras(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.produto}'
    

class EnderecoCobranca(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
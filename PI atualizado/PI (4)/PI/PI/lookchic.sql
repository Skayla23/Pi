CREATE database Lookchic;
USE Lookchic;
Create table usuario(
id INT primary key auto_increment,
clientenome varchar(100),
gmail varchar(45),
senha varchar(45),
CPF varchar(45),
carrinho_clientenome varchar(45),
enderec varchar(100),
datanasc date,
carrinho_codigo int
);

Create table produto(
codigo INT primary key auto_increment,
img varchar(45),
cor varchar(45),
produto_name varchar(45),
quant int,
preco_venda float
);

Create table pedido(
idpedido INT primary key auto_increment,
idcliente int,
idvendedor int,
idpagamento int,
valortotal float,
pedidocol varchar(45),
foreign key (idcliente) references usuario (id)
);

Create table Formaspagam(
id INT primary key auto_increment,
formasdepagam varchar(45)
);

Create table Pedido_Produto(
pedido_id INT primary key auto_increment,
produto_codigo int,
foreign key (pedido_id) references pedido (idpedido),
foreign key (produto_codigo) references produto (codigo)
);


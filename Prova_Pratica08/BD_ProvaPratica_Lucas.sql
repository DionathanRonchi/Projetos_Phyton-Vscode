create database lanchonete;
use lanchonete;

create table cardapio(
	id int auto_increment primary key,
	nome varchar(100) not null,
	preco decimal not null,
	tipo varchar(30),
    disponivel boolean
);

insert into cardapio values
(1, 'Suco', '5.00', 'comida', 10),
(2, 'Pizza', '100.00', 'comida', 50),
(3, 'Esponja', '2.00', 'cozinha',  20),
(4, 'Monitor', '1000.00', 'tecnologia',  30);

select*from cardapio;

#BUSCAR CLIENTES CUJO EMAIL CONTENHA "GMAIL"
select*from cardapio
where tipo like '%comida%';

#ATUALIZAR PRECO DE UM CLINETE PELO ID
update cardapio
set preco = '10'
where id = 3;


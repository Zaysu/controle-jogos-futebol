1° crie a database no postgree: football
2° execute o comando: 
	CREATE TABLE cadtimes (
	id serial PRIMARY KEY,
	nome VARCHAR (40) NOT null,
	gk VARCHAR ( 40 ) NOT null,
	lte VARCHAR ( 40 ) NOT null,
	zag1 VARCHAR ( 40 ) NOT null,
	zag2 VARCHAR ( 40 ) NOT null,
	ltd VARCHAR ( 40 ) NOT null,
	mei1 VARCHAR ( 40 ) NOT null,
	mei2 VARCHAR ( 40 ) NOT null,
	mei3 VARCHAR ( 40 ) NOT null,
	ata1 VARCHAR ( 40 ) NOT null,
	ata2 VARCHAR ( 40 ) NOT null,
	ata3 VARCHAR ( 40 ) NOT null
); 
para o cadastro do nome do time com nome dos jogadores

Caso queira fazer população do banco de forma manual:
INSERT INTO cadtimes (id, nome, gk, lte, zag1, zag2, ltd, mei1, mei2, mei3, ata1, ata2, ata3)
VALUES 
	('1','Vasco Da Gama', 'Thiago Rodrigues', 'Riquelme', 'Anderson Con', 'Quinteiro', 'Leo Kratos', 'Nene', 'Yuri Lara', 'Zé Gabriel', 'Gabriel Pec', 'Bruno Nazaro', 'Raniel'),
	('2','Flamengo', 'Hugo Souza', 'Rene', 'Leo Pereira', 'G. Henrique', 'F. Luiz', 'Thiago Maia', 'Gomes', 'Arrascaeta', 'Pedro', 'Gabriel Barbosa', 'Vitinho');
	
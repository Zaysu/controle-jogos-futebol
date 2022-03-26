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
3° execute o comando: 
	CREATE TABLE partidas (
	id serial PRIMARY KEY,
	clube VARCHAR (40) NOT null,
	localidade VARCHAR ( 40 ) NOT null,
	tempo VARCHAR ( 40 ) NOT null
);

4° execute o comando: 
	CREATE TABLE partidas (
	id serial PRIMARY KEY,
	time1 VARCHAR (40) NOT null,
	time2 VARCHAR ( 40 ) NOT null
);

5° Execute o Requeriments.txt para instalar as bibliotecas caso necessario

Recomendavel era usar sqlalchemy(percebi no decorrer do projeto) para fazer o auto incremento e foreignkey em algumas tabelas, mas fui pelo caminho do psycopg2, não vou ter tempo de terminar o projeto então estou encaminhando o repositorio do git, que vai ser atualizado com tempo para finalizar

Projeto cadastrando, Times com posições, Competições com local e data, e Cadastrando as partidas entre os times

Aluno: José Carlos Romão 
Matricula: 202110818
Curso: Eng. Software
Campus: Vassouras
Periodo: 3° (Até data atual 26/03/22)
Atualmente: Estagiario Desenvolvimento Web
Empresa: Simões Traduções Interpretações
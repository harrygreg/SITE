
```
insert into Curso (nome) values ('ANALISE E DESENVOLVIMENTO');
insert into Curso (nome) values ('Tecnologia em Jogos Digitais');
insert into Curso (nome) values ('SISTEMAS DE TI');
```

```
insert into Disciplina (nome, id_curso) values ('Lógica de Programaçao', 1);
insert into Disciplina (nome, id_curso) values ('Tecnologia Web', 1);
insert into Disciplina (nome, id_curso) values ('Unity', 2);
insert into Disciplina (nome, id_curso) values ('Gestão de Projetos', 3);
````

```
insert into Pessoa (nome, email, telefone, data_cadastro) values ('Cris Pereira', 'cris21@gmail.com', '(11) 1111111111', 2017-05-01);
insert into Pessoa (nome, email, telefone, data_cadastro) values ('Bruna Diniz', 'brunadiniz@hotmail.com', '(11) 1111111111', 2017-05-01);
insert into Pessoa (nome, email, telefone, data_cadastro) values ('Silmara Alencar', 'silmaraalencar@bol.com.br', '(11) 1111111111', 2017-05-01);
insert into Pessoa (nome, email, telefone, data_cadastro) values ('Jardel Freitas', 'jardel@jq.com.br', '(11) 1111111111', 2017-05-01);
```

```
insert into Aluno (id_pessoa, id_curso, data_inicio) values (1, 1, 2017-01-02);
insert into Aluno (id_pessoa, id_curso, data_inicio) values (2, 2, 2017-01-02);

```

```
insert into Professor (id_pessoa, id_disciplina, carga_horaria) values (4, 1, 80);
````

```
insert into Coordenador (id_pessoa) values (3);
```

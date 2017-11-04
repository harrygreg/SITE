
```
CREATE DATABASE SITE
```

```
use SITE;
```

```                                 
create table Curso (id int not null primary key auto_increment,
                    nome varchar(50) NOT NULL
);
```

```
create table Disciplina (id int not null primary key auto_increment,
                        nome varchar(50) not null,
                        id_curso int not null,
                        foreign key (id_curso) references Curso(id)
);
```

```
create table Pessoa (id int not null primary key auto_increment,
                     nome varchar(50) not null,
                     email varchar(50) not null,
                     telefone varchar(15) not null,
                     data_cadastro date not null
);
```
  
```
create table Aluno (id int not null primary key auto_increment,
                    id_pessoa int not null,
                    id_curso int not null,
                    data_inicio date,
                    foreign key (id_pessoa) references Pessoa(id),
                    foreign key (id_curso) references Curso(id)
);
```

```
create table Professor (id int not null primary key auto_increment,
                        id_pessoa int not null,
                        id_disciplina int not null,
                        carga_horaria int,
                        foreign key (id_pessoa) references Pessoa(id),
                        foreign key (id_disciplina) references Disciplina(id)
);
```
   
```
create table Coordenador (id int not null primary key auto_increment,
                          id_pessoa int not null,
                          foreign key (id_pessoa) references Pessoa(id)
);
```

                                            

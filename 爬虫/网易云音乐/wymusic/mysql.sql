 show variables like '%character%';

desc tablename

select count(*) form table_name 

character-set-server=utf8

alter table Playlist default character set utf8;

truncate table hotPlaylist;

drop table Playlist;
drop database wymusic;
create database wymusic;

热门歌单IP表
create table hotPlaylist
(
    id int unsigned,
    primary key(Id)
)
DELETE FROM hotPlaylist WHERE id = 2147483647

新表
create table hotPlaylistnew
(
    id int unsigned,
    primary key(Id)
)






-- ok
歌单表
create table PlayList
(List_Id Int unsigned,
List_Name varchar(50) not null,
Author_Id int unsigned not null,
List_img varchar(100) not null,
PlayCount int unsigned not null,
List_creatTime  Bigint not null,
List_updataTime  Bigint not null,
Description varchar(300),
SubscribedCount int not null,
ShareCount int not null,
CommentCount int not null,
primary key(List_Id)
)

--ok
create table Tags
(Tags_Id int auto_increment,
Tags_name varchar(30),
primary key(Tags_Id)
)

--ok
create table Relationsippt
(List_Id int unsigned not null,
Tags_Id int not null
)

--ok
create table Author
(Author_Id int unsigned,
Author_Name varchar(50)  not null,
Signature varchar(300),
city Int,
Author_img varchar(100),
primary key(Author_Id)
)

--ok
create table Relationsip
(List_Id int unsigned not null,
Music_Id int unsigned not null
)

--ok
歌曲表
create table Music
(Music_Id Int unsigned,
Music_Name varchar(50) not null,
Music_img varchar(100) not null,
Music_creatTime  Bigint not null,
Popularity int not null,
Description varchar(100),
Duration int not null,
Company varchar(50),
SubType varchar(50),
CommentCount int,
primary key(Music_Id)
)

--ok
歌手表
create table Singer
(Singer_Id int,
Singer_name varchar(50) not null,
primary key(Singer_Id)
)


评论表
create table Comment
(Comment_Id Bigint,
Comment_content varchar(200)  not null,
LikedCount int not null,
Music_Id int unsigned not null,
Author_Id int unsigned not null,
Comment_creatTime Bigint not null,
primary key(Comment_Id)
)


create table Relationsipms
(Music_Id int unsigned not null,
Singer_Id int not null
)



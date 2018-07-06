 show variables like '%character%';

character-set-server=utf8

alter table Playlist default character set utf8;

truncate table Playlist;

create database wymusic;

歌单表
create table Playlist
(List_Id Int,
List_Name varchar(50) not null,
Author_Id int not null,
List_img varchar(100) not null,
PlayCount int not null,
List_creatTime  Bigint,
List_updataTime  Bigint,
Description varchar(300),
SubscribedCount int,
ShareCount int,
CommentCount int,
Tags int,
primary key(List_Id)
)



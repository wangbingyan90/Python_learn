 show variables like '%character%';

desc tablename

select count(*) form table_name 

character-set-server=utf8

alter table Playlist default character set utf8;

truncate table hotPlaylist;

drop table hotPlaylist;

create database wymusic;

热门歌单IP表
create table hotPlaylist
(
    id int unsigned,
    primary key(Id)
)


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



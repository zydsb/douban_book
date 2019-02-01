create table `book_info`(
`id` int(10) not null auto_increment,
`title` varchar(100) not null default '',
`author` varchar(100) not null default '',
`score` float(3,1) not null default 0,
`scorenum` varchar(20) not null default 0,
`press` varchar(50) not null default '',
`isbn` bigint(20) not null default 0,
`price` float(7,4) not null default 0,
`publishyear` varchar(20) not null default '0',
`label` varchar(255) not null default 'book',
`pagecount` bigint(20) not null default 0 ,
primary key (id,isbn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='doubanBook详细信息表'

create table `book_desc`(
`id` int(10) not null auto_increment,
`isbn` bigint(20) not null default 0,
`authordesc` text,
`bookdesc` text,
`imageurl` text,
primary key (id,isbn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='doubanBook内容描述表'
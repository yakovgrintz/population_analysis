create schema IF NOT EXISTS elect_result;
use elect_result;
create table if not exists parties(
    id int auto_increment primary key,
    name_of_party varchar(100) not null,
    party_letters varchar(10) not null,
    political_opinion ENUM('right', 'left', 'unknown') NOT NULL,
    faction_union boolean not null default false,
    num_of_elect int not null default 1,
    nation enum('jewish','other')
);
create table if not exists settlements(
    id varchar(4) primary key ,
    name_of_settlements varchar(100) not null ,
    Foundation_year VARCHAR(4)


);

create table if not exists religions_code(
    religion_code ENUM('1', '2', '3', '4','5') primary key ,
    explanation varchar(20) not null

);
insert into religions_code(religion_code,explanation)
values ('1','יהודי
');
insert into religions_code(religion_code,explanation)
values ('2','לא יהודי
');
insert into religions_code(religion_code,explanation)
values ('3','שבט בדווי
');
insert into religions_code(religion_code,explanation)
values ('4','ישוב מעורב
');
insert into religions_code(religion_code,explanation)
values ('5','מקום
');
create table if not exists Construction_Planning_Committee(
    code_committee varchar(3) primary key ,
    name varchar(100) not null ,
    type enum('מחוזית','מקומית','אין נתונים','מרחבית')
);
create table if not exists Police_station(
    station_code varchar(10) primary key ,
    name_station varchar(100) not null ,
    machoz varchar(100) not null ,
    merchav varchar(100) not null


);
create table if not exists Type_of_settlement(
    type_code varchar(3) primary key ,
    type varchar(255) not null,
    type_yishuv ENUM('מקום', 'יישוב כפרי', 'יישוב עירוני') NOT NULL
);
CREATE table if not exists technical_settlement_information(
    code_yishuv varchar(4) not null  ,
    name_of_settlements varchar(100) not null ,
    religion_code ENUM('1', '2', '3', '4','5') NOT NULL,
    year_data varchar(4) not null,
    population int not null,
    jewish_and_other_pop int,
    jewish_pop int,
    arabic_pop int,
    Type_of_settlement varchar(3) not null ,
    police_station varchar(10) not null ,average_height int,
    Construction_Planning_Committee varchar(3) not null ,
    foreign key (religion_code) references religions_code(religion_code),
    foreign key (code_yishuv) references settlements(id),
    foreign key (Construction_Planning_Committee) references Construction_Planning_Committee(code_committee)
    ,foreign key (police_station) references Police_station(station_code),
    foreign key (Type_of_settlement) references Type_of_settlement(type_code)
);



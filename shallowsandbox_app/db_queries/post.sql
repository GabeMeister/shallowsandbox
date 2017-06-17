select * from user;

select * from post;
delete from post where id in (10, 11, 12, 13, 14, 15, 16);


select * from homework;

insert into post
(question, answer, creation_date, last_edit_date, user_id, homework_id) 
values
('another question 1', 'another answer', '2017-06-01 21:17:53.322785', '2017-06-01 21:17:53.322785', 60, 1);


insert into user (email, password) values ('gabe@gmail.com', 'fjeiwfwe');
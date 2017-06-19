select * from user;

update user set is_admin=1 where id=1;

select * from post;
delete from post where id in (11);


select * from homework;

select * from school where id=1657;

select * from course;



-- insert into post
-- (question, answer, creation_date, last_edit_date, user_id, homework_id) 
-- values
-- ('another question 1', 'another answer', '2017-06-01 21:17:53.322785', '2017-06-01 21:17:53.322785', 60, 1);


insert into user (email, password) values ('gabe@gmail.com', 'fjeiwfwe');
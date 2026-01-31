select(
case
    when g.grade<8 then "NULL"
    else s.name
    end) --wait
    as name, g.grade, s.marks
from grades g 
cross join students s 
where s.marks between g.min_mark and g.max_mark 
order by g.grade desc, 
case when g.grade between 8 and 10 then s.name end asc,
case when g.grade between 1 and 7 then s.marks end asc;


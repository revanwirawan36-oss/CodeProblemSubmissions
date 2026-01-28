select 
    max(case when occupation='doctor' then name end),
    max(case when occupation='professor' then name end),
    max(case when occupation='singer' then name end),
    max(case when occupation='actor' then name end)
from(
    select name, occupation, row_number() over(partition by occupation order by name) as rownum 
    from occupations
) as temptable
group by rownum
order by rownum

select h.hacker_id, h.name
from hackers h 
join submissions s on s.hacker_id=h.hacker_id
join challenges c on c.challenge_id=s.challenge_id
join difficulty d on c.difficulty_level=d.difficulty_level
where s.score=d.score --filter only the one who gets the full score
group by h.hacker_id, h.name 
having count(distinct s.challenge_id) > 1 --filter only the onw who have submitted more than one submission
order by count(distinct s.challenge_id) desc, h.hacker_id asc;

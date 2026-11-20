with base as (
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank() over (partition by e.departmentId order by salary desc) as salary_rank
    from 
        Employee e
        inner join Department d on e.departmentId = d.id
)

select 
    Department,
    Employee,
    Salary
from 
    base 
where 
    salary_rank <= 3
order by 1
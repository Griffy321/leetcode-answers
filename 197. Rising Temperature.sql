with base as (
    select 
        *,
        lag(temperature) over (order by cast(recordDate as date)) as prev_temp,
        lag(recordDate) over (order by cast(recordDate as date)) as prev_day

    from 
        Weather
)

select 
    id
from 
    base 
where 
    prev_temp < temperature 
    and datediff(recordDate, prev_day) = 1
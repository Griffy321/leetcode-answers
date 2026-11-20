with filtered as (
    select 
        i.pid, 
        i.tiv_2016 
    from 
        Insurance i
        left join Insurance i2 on i.lat = i2.lat and i.lon = i2.lon and i.pid != i2.pid
    where 
        i2.pid is null
        and i.tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1)
)

select 
    round(sum(s.tiv_2016), 2) as tiv_2016
from (
    select 
        pid,
        max(tiv_2016) as tiv_2016
    from 
        filtered
    group by pid
) s
with drivers as (
    select 
        *
    from 
        Users 
    where 
        role = "driver"
        and banned = "No"
)

, clients as (
    select 
        *
    from 
        Users 
    where 
        role = "client"
        and banned = "No"
)

, trips as (
    select 
        id as ride_id,
        t.client_id,
        t.driver_id,
        city_id,
        status,
        request_at
    from 
        Trips t
        inner join drivers d on t.driver_id = d.users_id
        inner join clients c on t.client_id = c.users_id
    where
        request_at between "2013-10-01" and "2013-10-03"
)

select 
    request_at as 'Day',
    round(SUM(trips.status != 'completed') / COUNT(*), 2) as 'Cancellation Rate'
from 
    trips 
group by request_at
order by request_at
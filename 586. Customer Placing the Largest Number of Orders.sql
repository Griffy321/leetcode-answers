with cust_ordres as (
    select 
        customer_number,
        count(*) as orders
    from 
        Orders
    group by customer_number 
)

select 
    customer_number 
from 
    cust_ordres
order by orders desc
limit 1
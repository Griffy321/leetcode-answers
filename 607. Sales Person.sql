with sales_orders as (
    select 
        s.name,
        count(case when c.name = "RED" then 1 end) as red_orders
    from 
        SalesPerson s
        left join Orders o on s.sales_id = o.sales_id
        left join Company c on o.com_id = c.com_id 
    group by s.name
)

select 
    name
from 
    sales_orders
where 
    red_orders = 0
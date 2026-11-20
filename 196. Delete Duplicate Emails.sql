delete 
    from 
        Person 
where Person.id in (
    select
        p.id
    from (
        select 
            id, 
            row_number() over (partition by email order by id) as rn
        from 
            Person
    ) p
    where 
        p.rn != 1
)
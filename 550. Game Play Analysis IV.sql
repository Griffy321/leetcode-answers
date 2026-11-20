with player_games as (
    select 
        *,
        row_number() over (partition by player_id order by event_date) as game_num
    from 
        Activity
)

, player_agg as (
    select 
        player_id,
        min(event_date) as game_1,
        max(event_date) filter (where game_num = 2) as game_2
    from 
        player_games
    group by player_id
)

select 
    round(sum(case when game_2 - game_1 = 1 then 1 else 0 end)::numeric / count(*), 2) as fraction 
from 
    player_agg
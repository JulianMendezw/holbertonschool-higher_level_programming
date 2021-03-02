-- Script that displays the max temperature of each state (ordered by State name).
SELECT state, value AS max_temp FROM temperatures GROUP BY state, value ORDER BY max_temp DESC LIMIT 3;


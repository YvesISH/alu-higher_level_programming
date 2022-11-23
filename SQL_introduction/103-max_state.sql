-- Display the max Temp of each state.
SELECT statet, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;

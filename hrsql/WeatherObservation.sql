SELECT ROUND(AVG(lat_n), 4) --avg because we could choose 2 different rownum
FROM (
    SELECT lat_n, 
           ROW_NUMBER() OVER (ORDER BY lat_n) as row_num, --this add rownum to the new table that we're gonna select
           COUNT(*) OVER () as total_count -- this add count to the new table
    FROM station
) AS ranked_data --this is the new table alias
WHERE row_num IN (FLOOR((total_count+1)/2), CEIL((total_count+1)/2)); --this select the rownum and takes the lat_n value in that rownum

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs (Song_Id string, Track_Id string, Title string, Artist_name string, Artist_Id string, Year int, Tempo double) row format delimited fields terminated by ",";

!echo -e "\n################# Loading Table #################\n";

LOAD DATA LOCAL INPATH "Songs.csv" OVERWRITE INTO TABLE Songs;

!echo -e "\n################# Starting Query #################\n";

SELECT Title, Artist_name, Tempo, Year FROM Songs GROUP BY Title, Artist_name, Tempo, Year;

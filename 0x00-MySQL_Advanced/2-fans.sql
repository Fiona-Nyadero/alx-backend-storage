-- country origins of bands ranking
-- by no. of non-unique fans

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY ORIGIN
ORDER BY nb_fans DESC;

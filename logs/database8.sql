SELECT ALL t0.c1 FROM t0 GROUP BY t0.c1;
--SELECT ALL t0.c1 FROM t0 NOT INDEXED GROUP BY t0.c1 HAVING GROUP_CONCAT(t0.c4) COLLATE NOCASE UNION ALL SELECT ALL t0.c1 FROM t0 GROUP BY t0.c1 HAVING (NOT (GROUP_CONCAT(t0.c4) COLLATE NOCASE)) UNION ALL SELECT ALL t0.c1 FROM t0 GROUP BY t0.c1 HAVING ((GROUP_CONCAT(t0.c4) COLLATE NOCASE) ISNULL);
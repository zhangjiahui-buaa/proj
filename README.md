## newer version sqlite 3.40.0

## older version sqlite 3.31.1

## db: testcases/database0.db (randomly generated by sqlancer)

## queries that trigger logical bug (TLP by sqlancer)
The following two queries should give the same result. It's true in sqlite3.31.1 but not sqlite3.40.0
 > SELECT t0.c2 FROM t0 GROUP BY t0.c2;

 > SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING ((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2)) UNION ALL SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING (NOT (((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2)))) UNION ALL SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING ((((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2))) ISNULL); 


## Reproduce the bug
    Basically you need two version of sqlite on your computer.
    I use conda to do this.
    First create an environment with sqlite3.40.0 : conda create -n newer sqlite=3.40.0
then run the abovementioned testcase. The first query returns 0.202107171794723 and 522035749 but second one only returns 0.202107171794723

    Then create an environment with sqlite3.30.0 : conda create -n older sqlite=3.30.0
    then run the abovementioned testcase. The two queries both return 522035749 and 0.202107171794723



import psycopg2


import logging

import pandas as pd
import logging


import xlsxwriter
#create file
outWorkbook=xlsxwriter.Workbook("out1.xlsx")

outsheet=outWorkbook.add_worksheet()
# Should have given some comments about the and it's solution such as "Solution for Problem Statement1 and connecting the database"
# from line 36-50 can be shorted using pandas dataframe "df=pd.DataFrame(cur.fetchall()) df=df.to_excel('out1.xlsx',header=["empno","ename","manager"],index=false)
class employees:
   def employ_manager(self):








    try:
 
     conn=psycopg2.connect(database="postgres",user="postgres",password="Hello@123")
     cur=conn.cursor()
     cur.execute("SELECT e.empno ,e.ename, m .ename manager FROM emp e LEFT  JOIN emp m   ON m.empno = e.mgr")




     rows=cur.fetchall()
     outsheet.write("A1","empno")
     outsheet.write("B1","ename")
     outsheet.write("C1","manager")




     x=1
     for r in rows:

      outsheet.write(x,0,r[0])
      outsheet.write(x,1,r[1])
      outsheet.write(x,2,r[2])
      x=x+1
    except Exception as e:
        logging.error("Error", e)




    finally:
       if conn is not None:
        outWorkbook.close()
        cur.close()
        conn.close()




if __name__ == '__main__':
    conn = None
    cur = None
    emp = employees()
    emp.employ_manager()


import psycopg2
import xlsxwriter
#create file
outWorkbook=xlsxwriter.Workbook("out2.xlsx")

outsheet=outWorkbook.add_worksheet()

class compensation:
  def total_compensation(self):

   try:

    conn = psycopg2.connect(database="postgres", user="postgres", password="Hello@123")
    cur = conn.cursor()
    cur.execute("select emp.ename, dept.dname, emp.empno ,(case when enddate is not null then ((enddate-startdate+1)/30)*jobhist.sal else ((current_date-startdate+1)/30)*jobhist.sal end)as Total_Compensation,(case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno")

    row=cur.fetchall()
    outsheet.write("A1", "ename")
    outsheet.write("B1", "dname")
    outsheet.write("C1", "empno")
    outsheet.write("D1", "Total_compensation")
    outsheet.write("E1", "Months_spent")
    x=1
    for r in row:
     outsheet.write(x,0,r[0])
     outsheet.write(x,1,r[1])
     outsheet.write(x,2,r[2])
     outsheet.write(x,3,r[3])
     outsheet.write(x,4,r[4])
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
    salary = compensation()
    salary.total_compensation()
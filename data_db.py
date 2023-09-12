import mysql.connector as m

class dbconnect:
    def __init__(self) -> None:
        self.host="localhost"
        self.user="root"
        self.password="root"
        self.database="sample"
        
    def connection(self):
        try:
            self.g=m.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            
            return True
        except:
            return False
    def createtable(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                ad.execute("CREATE TABLE sample1( ID int AUTO_INCREMENT PRIMARY KEY,LastName varchar(255) NOT NULL,FirstName varchar(255),Age int)")
                
                return True
            except IOError:
                
                return Exception
        else :
            return ConnectionError
        
    def adddata(self,fname,surname,age):
        if self.connection()==True:
            ad=self.g.cursor()
            val=(fname,surname,age)
            qr="INSERT INTO sample1 (Lastname,Firstname,Age) VALUES (%s, %s,%s)"
            try:
                ad.execute(qr,val)
                self.g.commit()
                return True
            except IOError:
                
                return Exception
        else :
            return ConnectionError
    def deletetable(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                ad.execute("DROP TABLE sample1")
                print("DELETED")
            except IOError:
                return Exception
    def readdata(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                t=ad.execute("Select * from sample1")
                y=ad.fetchall()
                return y
                # for i in y:
                    # return i
            except IOError:
                return Exception
    def deldata(self,id):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                cmd=(f"delete from sample1 where ID={id}")
                ad.execute(cmd)
                self.g.commit()
                y=ad.fetchall()
                return True
            except IOError:
                return Exception
    def updatedata(self,sname,fname,age,id):
        if self.connection()==True:
            ad=self.g.cursor()
            a=0
            sn=None
            fn=None
            try:
                if sname!=None:
                    sn=sname
                if age!=0:
                    a=age
                if fname!=0:
                    fn=fname

                cmd=(f"update sample1 set FirstName='{fn}',LastName='{sn}',Age={a} where ID={id}")
                ad.execute(cmd)
                self.g.commit()
                y=ad.fetchall()
                return True
            except IOError:
                return Exception


# if __name__=="__main__":
#     ob=dbconnect()
#     u=ob.readdata()
#     print(u)
   
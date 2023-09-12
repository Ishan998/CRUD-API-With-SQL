import json
from flask import Flask,request,render_template
import data_db as db
import numpy as np
from data_db import dbconnect
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        x={'operation':'display home','name':'ishan','surname':'srivastava','age':27}
        pp=json.dumps(x)
        return render_template("example.html")
    elif request.method=='POST':
        s=request.json
        print(s)
        
        return json.dumps(s)
@app.route('/read',methods=['GET'])
def read():
    
    
    try:
        yu=dbconnect().readdata()
        p=[]
        res={}
        data=['id','surname','firstname','age']
        
        for i in yu:
            res = {data[j]: i[j] for j in range(len(i))}        
            # print(res)
            p.append(res)
        pp=json.dumps(p)
        return pp
    except IOError:
        return Exception
@app.route('/delete',methods=['DELETE'])
def delet():
    res=request.json
    # l=None
    for key,val in list(res.items()):
        if key =="id":
            # l=val
            yu=dbconnect().deldata(id=val)
            if yu:
                res.update({'status':'Deleted successfully'})
            else:
                res.update({'status':'operation unsuccesfull'})
    pp=json.dumps(res)
    return pp

@app.route('/updated',methods=['PUT'])
def updat():
    res=request.json
    fname=''
    sname=''
    age=0
    for key,val in list(res.items()):
        if key=='id':
                id=val
        if key =="firstname":
            fname=val
        if key=='surname':
            sname=val
        if key=='age':
            age=val
    yu=dbconnect().updatedata(fname=fname,sname=sname,age=age,id=id)
    if yu:
        res.update({'status':'Data Updated successfully'})
    else:
        res.update({'status':'Data Updated unsuccesfull'}) 
    print(res)


    pp=json.dumps(res)
    print(pp)
    return pp

@app.route('/create',methods=['POST'])
def create():
    try:
        t=db.dbconnect()
        res=request.json
        fname=None
        sname=None
        age=0
        for key,value in list(res.items()):
           
            if key=='firstname':
                    fname=value
            if key=='surname':
                sname=value
            if key=='age':
                age=value
        save=t.adddata(fname=fname,surname=sname,age=age)
        if save:
            res.update({'operation':'user created'})
        else:
            res.update({'operation':'user not created'})
        pp=json.dumps(res)
        return pp
    except IOError:
        return Exception

if __name__=="__main__":
    app.debug=True
    app.run(port=3030)


import os
import pickle
import pandas as pd
import math
import random

datafile="ds.csv"
modelfile="model.pkl"
histfile="history.csv"

xtra=0
num=50

def loaddata():
    try:
        if os.path.exists(datafile)==False:
            print("data file not found")
            exit()
        try:
            df=pd.read_csv(datafile,encoding="utf-8")
        except:
            df=pd.read_csv(datafile,encoding="latin1")
        cols=[]
        for c in df.columns:
            name=c.strip()
            name=name.lower()
            cols.append(name)
        df.columns=cols
        if "phrase" not in df.columns or "sentiment" not in df.columns:
            print("wrong dataset format")
            exit()
        df["phrase"]=df["phrase"].astype(str)
        df["sentiment"]=df["sentiment"].astype(str)
        df["sentiment"]=df["sentiment"].str.lower()
        temp=1
        temp=temp+1
        return df
    except:
        print("error loading data")
        exit()

def trainmodel(df):
    try:
        x=df["phrase"]
        y=df["sentiment"]
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        vec=TfidfVectorizer()
        xvec=vec.fit_transform(x)
        model=LogisticRegression()
        model.fit(xvec,y)
        data={}
        data["vec"]=vec
        data["model"]=model
        f=open(modelfile,"wb")
        pickle.dump(data,f)
        f.close()
        print("model trained")
        return data
    except:
        print("training error")
        exit()

def loadmodel():
    try:
        if os.path.exists(modelfile):
            f=open(modelfile,"rb")
            data=pickle.load(f)
            f.close()
            return data
        else:
            df=loaddata()
            data=trainmodel(df)
            return data
    except:
        print("model load error")
        exit()

def savehist(txt,res):
    try:
        exist=os.path.exists(histfile)
        f=open(histfile,"a")
        if exist==False:
            f.write("text,result\n")
        line='"'+txt+'",'+res+"\n"
        f.write(line)
        f.close()
    except:
        print("history save error")

def predict(data,txt):
    try:
        vec=data["vec"]
        model=data["model"]
        arr=[]
        arr.append(txt)
        x=vec.transform(arr)
        res=model.predict(x)
        out=res[0]
        return out
    except:
        print("prediction error")
        return "error"

def showabout():
    print("")
    print("AI Sentiment Tool")
    print("basic ml project")
    print("saves history also")
    print("")

def showhelp():
    print("")
    print("1 enter text")
    print("2 about")
    print("3 help")
    print("4 history")
    print("0 exit")
    print("")

def showhist():
    try:
        if os.path.exists(histfile)==False:
            print("no history")
            return
        f=open(histfile,"r")
        lines=f.readlines()
        f.close()
        if len(lines)<=1:
            print("no data")
            return
        print("")
        print("last results")
        print("")
        cnt=0
        for l in lines:
            cnt=cnt+1
        start=cnt-5
        if start<0:
            start=0
        i=0
        for l in lines:
            if i>=start:
                print(l.strip())
            i=i+1
    except:
        print("error reading history")

def main():
    data=loadmodel()
    a=10
    b=a
    print("start")
    while True:
        print("")
        print("1. Enter Text")
        print("2. About")
        print("3. Help")
        print("4. View History")
        print("0. Exit")
        ch=input("choice: ")
        if ch=="1":
            txt=input("enter: ")
            if txt=="":
                print("empty input")
            else:
                res=predict(data,txt)
                print("result:",res)
                savehist(txt,res)
        else:
            if ch=="2":
                showabout()
            elif ch=="3":
                showhelp()
            elif ch=="4":
                showhist()
            elif ch=="0":
                print("bye")
                break
            else:
                print("wrong choice")

if __name__=="__main__":
    main()
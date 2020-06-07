##########################################PREDICTION OF EXPENSE CATEGORY WISE#######################################################
import sqlite3 as sq
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class Predict():
    def __init__(self):
        self.foodString='select amount from expense where ex_name in ("Food") and name in ("megha9")'
        self.transportationString='select amount from expense where ex_name in ("Transportation") and name in ("megha9")'
        self.carString='select amount from expense where ex_name in ("Car") and name in ("megha9")'
        self.entertainmentString='select amount from expense where ex_name in ("Entertainment") and name in ("megha9")'
        self.shoppingString='select amount from expense where ex_name in ("Shopping") and name in ("megha9")'
        self.taxString='select amount from expense where ex_name in ("Tax") and name in ("megha9")'
        self.electronicsString='select amount from expense where ex_name in ("Electronics") and name in ("megha9")'
        self.healthString='select amount from expense where ex_name in ("Health") and name in ("megha9")'
        self.beautyString='select amount from expense where ex_name in ("Beauty") and name in ("megha9")'
        self.educationString='select amount from expense where ex_name in ("Education") and name in ("megha9")'
        self.sportsString='select amount from expense where ex_name in ("Sports") and name in ("megha9")'
        self.socialString='select amount from expense where ex_name in ("Social") and name in ("megha9")'
        self.giftString='select amount from expense where ex_name in ("Gift") and name in ("megha9")'
        self.officeString='select amount from expense where ex_name in ("Office") and name in ("megha9")'
        self.othersString='select amount from expense where ex_name in ("Others") and name in ("megha9")'
        self.billString='select amount from expense where ex_name in ("Bill") and name in ("megha9")'
        self.homeString='select amount from expense where ex_name in ("Home") and name in ("megha9")'
        self.clothingString='select amount from expense where ex_name in ("Clothing") and name in ("megha9")'
        self.insuranceString='select amount from expense where ex_name in ("Insurance") and name in ("megha9")'
            
        self.client=sq.connect(r"user.db")
        self.cur=self.client.cursor()
    def getfood(self,value):
        self.cur.execute(self.foodString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def gettransportation(self,value):
        self.cur.execute(self.transportationString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getcar(self,value):
        self.cur.execute(self.carString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getentertainment(self,value):
        self.cur.execute(self.entertainmentString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getshopping(self,value):
        self.cur.execute(self.shoppingString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def gettax(self,value):
        self.cur.execute(self.taxString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getelectronics(self,value):
        self.cur.execute(self.electronicsString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def gethealth(self,value):
        self.cur.execute(self.healthString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getbeauty(self,value):
        self.cur.execute(self.beautyString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def geteducation(self,value):
        self.cur.execute(self.educationString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getsports(self,value):
        self.cur.execute(self.sportsString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getsocial(self,value):
        self.cur.execute(self.socialString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getgift(self,value):
        self.cur.execute(self.giftString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getoffice(self,value):
        self.cur.execute(self.officeString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getothers(self,value):
        self.cur.execute(self.othersString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getbill(self,value):
        self.cur.execute(self.billString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def gethome(self,value):
        self.cur.execute(self.homeString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getclothing(self,value):
        self.cur.execute(self.clothingString+'and month={0}'.format(value))
        return self.cur.fetchall()
    def getinsurance(self,value):
        self.cur.execute(self.insuranceString+'and month={0}'.format(value))
        return self.cur.fetchall()

P=Predict()
monthlyExpense=[]
totalExpense=[]
for j in range(1,13):
    foodExpense,officeExpense,transExpense, entertainExpense,shoppingExpense,taxExpense, elecExpense,healthExpense=0,0,0,0,0,0,0,0
    eduExpense, sportsExpense,socialExpense, giftExpense,othersExpense,billExpense,homeExpense,clothExpense, insuranceExpense, carExpense,beautyExpense=0,0,0,0,0,0,0,0,0,0,0
    foodExpense=np.sum(np.array([i[0] for i in P.getfood(j)]))
    officeExpense=np.sum(np.array([i[0] for i in P.getoffice(j)]))
    transExpense= np.sum(np.array([i[0] for i in P.gettransportation(j)]))
    entertainExpense=np.sum(np.array([i[0] for i in P.getentertainment(j)]))
    shoppingExpense=np.sum(np.array([i[0] for i in P.getshopping(j)]))
    taxExpense=np.sum(np.array([i[0] for i in P.gettax(j)]))
    elecExpense=np.sum(np.array([i[0] for i in P.getelectronics(j)]))
    healthExpense=np.sum(np.array([i[0] for i in P.gethealth(j)]))
    beautyExpense=np.sum(np.array([i[0] for i in P.getbeauty(j)]))
    eduExpense=np.sum(np.array([i[0] for i in P.geteducation(j)]))
    sportsExpense=np.sum(np.array([i[0] for i in P.getsports(j)]))
    socialExpense=np.sum(np.array([i[0] for i in P.getsocial(j)]))
    giftExpense=np.sum(np.array([i[0] for i in P.getgift(j)]))
    othersExpense=np.sum(np.array([i[0] for i in P.getothers(j)]))
    billExpense=np.sum(np.array([i[0] for i in P.getbill(j)]))
    homeExpense=np.sum(np.array([i[0] for i in P.gethome(j)]))
    clothExpense=np.sum(np.array([i[0] for i in P.getclothing(j)]))
    insuranceExpense=np.sum(np.array([i[0] for i in P.getinsurance(j)]))
    carExpense=np.sum(np.array([i[0] for i in P.getcar(j)]))
    monthlyExpense.append([foodExpense,officeExpense,transExpense, entertainExpense,shoppingExpense,taxExpense, elecExpense,healthExpense,beautyExpense,eduExpense, sportsExpense,socialExpense, giftExpense,othersExpense,billExpense,homeExpense,clothExpense,insuranceExpense, carExpense])
    totalExpense.append(sum([foodExpense,officeExpense,transExpense, entertainExpense,shoppingExpense,taxExpense, elecExpense,healthExpense,eduExpense, sportsExpense,socialExpense, giftExpense,othersExpense,billExpense,homeExpense,clothExpense,insuranceExpense, carExpense,beautyExpense]))
monthlyExpense=np.array(monthlyExpense)
totalExpense=np.array(totalExpense)
print(totalExpense)
print(monthlyExpense)


x_tr,x_ts,y_tr,y_ts=train_test_split(monthlyExpense,totalExpense,test_size=0.25,random_state=0)
algo=LinearRegression()
algo.fit(x_tr,y_tr)
print(algo.score(x_ts,y_ts))
result=algo.predict(x_ts)
print(sum(result)/len(result),sep='\n')


fx_tr,fx_ts,fy_tr,fy_ts=train_test_split(monthlyExpense[:,0].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo1=LinearRegression()
algo1.fit(fx_tr,fy_tr)
print(algo1.score(fx_ts,fy_ts))
result1=algo1.predict(fx_ts)
print(sum(result1)/len(result1),sep='\n')


ox_tr,ox_ts,oy_tr,oy_ts=train_test_split(monthlyExpense[:,1].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo2=LinearRegression()
algo2.fit(ox_tr,oy_tr)
print(algo2.score(ox_ts,oy_ts))
result2=algo2.predict(ox_ts)
print(result2,sep='\n')


tx_tr,tx_ts,ty_tr,ty_ts=train_test_split(monthlyExpense[:,2].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo3=LinearRegression()
algo3.fit(tx_tr,ty_tr)
print(algo3.score(tx_ts,ty_ts))
result3=algo3.predict(tx_ts)
print(result3,sep='\n')


ex_tr,ex_ts,ey_tr,ey_ts=train_test_split(monthlyExpense[:,3].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo4=LinearRegression()
algo4.fit(ex_tr,ey_tr)
print(algo4.score(ex_ts,ey_ts))
result4=algo4.predict(ex_ts)
print(result4,sep='\n')


sx_tr,sx_ts,sy_tr,sy_ts=train_test_split(monthlyExpense[:,4].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo5=LinearRegression()
algo5.fit(sx_tr,sy_tr)
print(algo5.score(sx_ts,sy_ts))
result5=algo5.predict(sx_ts)
print(result5,sep='\n')


tax_tr,tax_ts,tay_tr,tay_ts=train_test_split(monthlyExpense[:,5].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo6=LinearRegression()
algo6.fit(tax_tr,tay_tr)
print(algo6.score(tax_ts,tay_ts))
result6=algo6.predict(tax_ts)
print(result6,sep='\n')


ex_tr,ex_ts,ey_tr,ey_ts=train_test_split(monthlyExpense[:,6].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo7=LinearRegression()
algo7.fit(ex_tr,ey_tr)
print(algo7.score(ex_ts,ey_ts))
result7=algo7.predict(ex_ts)
print(result7,sep='\n')


hx_tr,hx_ts,hy_tr,hy_ts=train_test_split(monthlyExpense[:,7].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo8=LinearRegression()
algo8.fit(hx_tr,hy_tr)
print(algo8.score(hx_ts,hy_ts))
result8=algo8.predict(hx_ts)
print(result8,sep='\n')


edx_tr,edx_ts,edy_tr,edy_ts=train_test_split(monthlyExpense[:,9].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo9=LinearRegression()
algo9.fit(edx_tr,edy_tr)
print(algo9.score(edx_ts,edy_ts))
result9=algo9.predict(edx_ts)
print(result9,sep='\n')


sx_tr,sx_ts,sy_tr,sy_ts=train_test_split(monthlyExpense[:,10].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo10=LinearRegression()
algo10.fit(sx_tr,sy_tr)
print(algo10.score(sx_ts,sy_ts))
result10=algo10.predict(sx_ts)
print(result10,sep='\n')


sox_tr,sox_ts,soy_tr,soy_ts=train_test_split(monthlyExpense[:,11].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo11=LinearRegression()
algo11.fit(sox_tr,soy_tr)
print(algo11.score(sox_ts,soy_ts))
result11=algo11.predict(sox_ts)
print(result11,sep='\n')


gx_tr,gx_ts,gy_tr,gy_ts=train_test_split(monthlyExpense[:,12].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo12=LinearRegression()
algo12.fit(gx_tr,gy_tr)
print(algo12.score(gx_ts,gy_ts))
result12=algo12.predict(gx_ts)
print(result12,sep='\n')


ox_tr,ox_ts,oy_tr,oy_ts=train_test_split(monthlyExpense[:,13].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo13=LinearRegression()
algo13.fit(ox_tr,oy_tr)
print(algo13.score(ox_ts,oy_ts))
result13=algo13.predict(ox_ts)
print(result1,sep='\n')


bx_tr,bx_ts,by_tr,by_ts=train_test_split(monthlyExpense[:,14].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo14=LinearRegression()
algo14.fit(bx_tr,by_tr)
print(algo14.score(bx_ts,by_ts))
result14=algo14.predict(bx_ts)
print(result14,sep='\n')


hx_tr,hx_ts,hy_tr,hy_ts=train_test_split(monthlyExpense[:,15].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo15=LinearRegression()
algo15.fit(hx_tr,hy_tr)
print(algo15.score(hx_ts,hy_ts))
result15=algo15.predict(hx_ts)
print(result15,sep='\n')


cx_tr,cx_ts,cy_tr,cy_ts=train_test_split(monthlyExpense[:,16].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo16=LinearRegression()
algo16.fit(cx_tr,cy_tr)
print(algo16.score(cx_ts,cy_ts))
result16=algo16.predict(cx_ts)
print(result1,sep='\n')


ix_tr,ix_ts,iy_tr,iy_ts=train_test_split(monthlyExpense[:,17].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo17=LinearRegression()
algo17.fit(ix_tr,iy_tr)
print(algo17.score(ix_ts,iy_ts))
result17=algo17.predict(ix_ts)
print(result17,sep='\n')


cax_tr,cax_ts,cay_tr,cay_ts=train_test_split(monthlyExpense[:,18].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo18=LinearRegression()
algo18.fit(cax_tr,cay_tr)
print(algo18.score(cax_ts,cay_ts))
result18=algo18.predict(cax_ts)
print(result18,sep='\n')


bex_tr,bex_ts,bey_tr,bey_ts=train_test_split(monthlyExpense[:,18].reshape(-1,1),totalExpense,test_size=0.25,random_state=0)
algo19=LinearRegression()
algo19.fit(bex_tr,bey_tr)
print(algo19.score(bex_ts,bey_ts))
result19=algo19.predict(bex_ts)
print(result19,sep='\n')



import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())
vc = pd.merge(visits,cart,how='left')
cnt1 = len(vc)
print(cnt1)
vcnull = vc[vc.cart_time.isnull()]
print(len(vcnull))
cnt2 = float(len(vcnull))/len(vc)
print(cnt2)

cc = pd.merge(cart,checkout,how='left')
cnt3 = len(cc)
print(cnt3)
ccnull = cc[cc.checkout_time.isnull()]
print(len(ccnull))
cnt4 = float(len(ccnull))/len(cc)
print(cnt4)

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())
pnull = all_data[all_data.purchase_time.isnull()]
cnt5 = float(len(pnull))/len(ccnull)
print(cnt5)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
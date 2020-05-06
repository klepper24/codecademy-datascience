import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
utm_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_count)
ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True]/ (clicks_pivot[True]+clicks_pivot[False])
cnt = ad_clicks.groupby('experimental_group').user_id.count()
cnt2 = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
15
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

clicks_by_source2 = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
clicks_pivot2 = clicks_by_source2.pivot(columns='is_click',index='day',values='user_id').reset_index()
clicks_pivot2['percent_clicked'] = clicks_pivot2[True]/ (clicks_pivot2[True]+clicks_pivot2[False])


clicks_by_source3 = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
clicks_pivot3 = clicks_by_source3.pivot(columns='is_click',index='day',values='user_id').reset_index()
clicks_pivot3['percent_clicked'] = clicks_pivot3[True]/ (clicks_pivot3[True]+clicks_pivot3[False])

print(clicks_pivot3)
print(clicks_pivot2)


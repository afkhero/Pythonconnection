import pymapd as py
import matplotlib.pyplot as plt

user_str = 'I97D12D9D7268474D874'
password_str = 'quzPy63R6kAG4BTeQ0Y5DxnsO3sZl7pehv6u673v'
host_str = 'use2-api.mapd.cloud'
dbname_str = 'mapd'
connection = py.connect(user=user_str, password=password_str, host=host_str, dbname=dbname_str, port=443, protocol='https')
# connection = py.connect(host=host_str, dbname=dbname_str, port=443, protocol='https')


query = "SELECT movement_id FROM san_francisco_taz_26 LIMIT 100"
df = connection.execute(query)
df2 = df.fetchall()

plt.plot(df2)
plt.show()

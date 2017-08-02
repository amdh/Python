
# coding: utf-8

# In[4]:

import phoenixdb


# In[5]:

database_url = 'http://<ip>:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)


# In[ ]:

cursor = conn.cursor()
cursor.execute("UPSERT INTO test VALUES (?, ? ,?)", (2, 'test',2017-07-28T09:52:40.0000659-07:00))
cursor.execute("select * from test")
print(cursor.fetchall())


# In[ ]:

cursor = conn.cursor()
cursor.execute("CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, username VARCHAR)")
cursor.execute("UPSERT INTO users VALUES (?, ?)", (2, 'user'))
cursor.execute("select * from users")
print(cursor.fetchall())





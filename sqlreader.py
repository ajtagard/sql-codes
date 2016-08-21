import csv
import numpy as np
import sqlite3

conn = sqlite3.connect('survey4.db')
c = conn.cursor()

data = list(csv.reader(open('adddata.csv', 'rb'), delimiter = ','))

label = data[0][:]
measurement = data[1:np.shape(data)[0]][:]
measurement = np.array(measurement, dtype='float')


#print 'sqlite3 survey2.db'
c.execute("INSERT INTO Person values('olm', 'Robert', 'Olmstead');")

for m in measurement:
    c.execute("INSERT INTO Survey values({}, 'olm', 'temp', {});" .format(m[0], m[1]))
    print "INSERT INTO Survey values({}, 'olm', 'temp', {});" .format(m[0], m[1])

conn.commit()
c.close()
conn.close()

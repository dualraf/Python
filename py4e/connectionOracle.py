import getpass
import oracledb

connection = oracledb.connect(
    user="system",
    password="zair",
    dsn="system@//localhost:1521/xe")#se saca de las propiedades de la base de Datos,Detalles de Conexion

print("Succesfully connected to Orable Database")

cursor = connection.cursor()

cursor.execute("""
    begin
        execute immediate 'drop table counts';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    CREATE TABLE COUNTS(
        ORG VARCHAR2(128),
        COUNT NUMBER)""")

fname = input('Enter file name:')
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1].split('@')
    organization = email[1]
    cursor.execute('SELECT count FROM Counts WHERE org = :0 ', (organization,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute("""INSERT INTO COUNTS (org,COUNT) VALUES (:0,1)""",(organization,))
    else:
        cursor.execute("UPDATE COUNTS SET COUNT=COUNT + 1 WHERE org = :0",(organization,))
    connection.commit()

sqlstr = 'SELECT org, COUNT FROM COUNTS ORDER BY count DESC'
for row in cursor.execute(sqlstr):
    print(row[0],row[1])
cursor.close()

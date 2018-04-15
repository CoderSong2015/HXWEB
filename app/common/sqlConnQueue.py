import queue
import pymysql
class sqlConnQueue():
    def __init__(self, conNumber = None, property = None):
        if conNumber == None or property == None:
            #meed to be logged
            print('sql queue init error')
        self.conNumber = conNumber
        self.property = property
        self.queue = queue.Queue()
        self.initConnection()

    def initConnection(self):
        for i in range(self.conNumber):
            db = pymysql.connect(  host = self.property['host']
                             , user = self.property['user']
                             , password = self.property['password']
                             , db=self.property['db']
                             , port=self.property['port'])

            print(type(db))
            self.queue.put(db)

    def getConn(self):
        return self.queue.get()

    def putConn(self, dbConn):
        if  not isinstance(pymysql.connections.Connection,dbConn):
            #log
            pass
        return self.queue.put(dbConn)


if __name__ == '__main__':
    property = { 'host':'localhost',
                 'user':'root',
                 'password':'123456',
                 'db':'song',
                 'port':3306,
                }
    print('get queue')
    sql = sqlConnQueue(3,property)
    conn = sql.getConn()
    stmt = conn.cursor()
    stmt.execute("select * from test")
    conn.commit()

    rs = stmt.fetchall()
    print(rs)

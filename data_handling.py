import sqlite3

ratings = {'BB':0,'BBB':1,'BBB+':1.25,'A-':1.75,'A':2,'A+':2.25,'AA-':2.5,'AA2':2.75,'AA':3,'AA+':3.25,'AAA-':3.75,'AAA':4}

def get_con():
    return sqlite3.connect('D:/prediction/bonds.db')

def day_format(s):
    if '-' in s:
        return s[:4]+s[5:7]+s[8:]
    else:
        return s[:4] + '-' + s[4:6] + '-' + s[6:]

def get_trading_days(option=0):
    """
    :param option: 0:Transactions 1:bonds
    :return: list of trading days
    """
    tables = ["'Transaction'","bond","implicit"]
    names =['tdate','trade_dt',"trade_dt"]
    cur = get_con().cursor()
    q_str = f"select distinct {names[option]} from {tables[option]} order by {names[option]} ASC"
    cur.execute(q_str)
    return list(cur.fetchall())

def get_all_bonds():
    cur = get_con().cursor()
    q_str = f"select distinct id from bond"
    cur.execute(q_str)
    return list(cur.fetchall())

def get_rating(con,bond_id,trade_dt):
    cur = con.cursor()
    cur.execute(f"select rating from implicit where trade_dt='{trade_dt}' and id='{bond_id}'")
    a = list(cur.fetchall())[0][0]
    if not a or a not in ratings:
        return None
    else:
        return ratings[a]
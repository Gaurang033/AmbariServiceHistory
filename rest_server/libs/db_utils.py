import os
import pandas as pd
import sqlite3
import config

__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = '%s/../database/hadoop.db' % CURRENT_DIR

def get_db():
    return sqlite3.connect(DATABASE)


def _query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()

    # cur.close()
    db.close()
    return (rv[0] if rv else None) if one else rv


def _get_current_status(service_name):
    query="select status from services where service_name='%s' and dte=date('now')" % service_name
    return _query_db(query)


def _insert_new_status(status):
    query = 'insert into services values(date("now"), "%s", "%s")' % (status.get('service_name'), status.get('status'))
    return _query_db(query)


def _update_status(service_name, status):
    query = 'update services set status="%s" where service_name="%s" and dte=date("now")' % (status, service_name)
    return _query_db(query)


def update_table(status):
    previous_status = _get_current_status(status.get('service_name'))
    if previous_status:
        previous_status = list(previous_status[0])
        previous_status.append(status.get('status'))
        _update_status(status.get('service_name'), "".join(previous_status))
    else:
        _insert_new_status(status)

    print(previous_status)


def get_status_data():
    res = _query_db("select * from services order by dte desc")
    df = pd.DataFrame(res)
    interval_min=int(config.fetch_interval / 60)

    # json = ({_: {k: [int(v) for v in list(v)] for k, v in zip(g[0], g[2])} for _, g in df.groupby(1)})
    json = ({_: {k: {"downTime":v.count("0"),
                     "totalTime": len(v),
                     "currentStatus": int(v[-1])
                     } for k, v in zip(g[0], g[2])} for _, g in df.groupby(1)})

    return json


if __name__ == '__main__':

    get_status_data()
    print(res)


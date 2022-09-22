from elasticsearch import Elasticsearch
import elasticsearch.exceptions
import json
import logging
import psycopg2
import random
import time

logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    with psycopg2.connect(dbname='bidask', user='postgres', password='secretpass', host='postgres') as conn:
        with conn.cursor() as cur:
            es = Elasticsearch("http://elastic:9200")
            time.sleep(20)
            es.indices.create(index='bidask')
            ii = 0
            while True:
                ii += 1
                msg = dict()
                for level in range(50):
                    (
                        msg[f"bid_{str(level).zfill(2)}"],
                        msg[f"ask_{str(level).zfill(2)}"],
                    ) = (
                        random.randrange(1, 100),
                        random.randrange(100, 200),
                    )
                msg["stats"] = {
                    "sum_bid": sum(v for k, v in msg.items() if "bid" in k),
                    "sum_ask": sum(v for k, v in msg.items() if "ask" in k),
                }
                logger.info(f"{json.dumps(msg)}")
                if msg["bid_01"]+msg["ask_01"]<120:
                    es.index(index='bidask', ignore=400, doc_type='bidask', id=ii, body=json.dumps(msg))
                query_sql = """ insert into json_table select * from json_populate_record(NULL::json_table, %s); """
                cur.execute(query_sql, (json.dumps(msg),))
                conn.commit()
                time.sleep(0.001)

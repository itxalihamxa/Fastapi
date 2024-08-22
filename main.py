from fastapi import FastAPI
from roouters import post, auth, user
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI(
    title= 'POSTGRES QUERYS IN FASTAPI ',
    description = "RAW QUERYS IN FASTAPI",
    version="1.0.0",
    contact= {
        "name": "lms",
        "email": "lms@example.com",
    },
    license_info= {
        "name": "lms",
    },
)


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='db', user='admin',
                                password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database conncetion was successful')
        break
    except Exception as error:
        print("connection failed")
        print("Error: ", error)
        time.sleep(5)



app.include_router(auth.router)

app.include_router(user.router)

app.include_router(post.router)
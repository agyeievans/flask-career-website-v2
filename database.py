from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://y1s7oi7pzhp7aytgbxbm:pscale_pw_cFxNXyffbqZZgzWhqJWoMkXuSEGcPgdCTArE3fqrZOe@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine( 
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }   
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))     
        return jobs
    
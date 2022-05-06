import psycopg2

def load_data():
    try:
        # dbname=restsdb
        conn = psycopg2.connect("host=localhost user=postgres password=secret")
    except:
        return "Unable to connect to database"
    print("Accessed database")

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS restaurants")
    # cur.execute('''CREATE TABLE RESTAURANTS();''')
    cur.execute('''CREATE TABLE restaurants
        (CAMIS INT PRIMARY KEY  NOT NULL,
        DBA         TEXT        NOT NULL,
        BORO        VARCHAR(20),
        ZIPCODE     CHAR(5),
        SCORE       INT         NOT NULL,
        GRADE       CHAR(1));''')

    with open('DOHMH_New_York_City_Restaurant_Inspection_Results-sampled.csv') as f:
        print(f.readline())
        # cur.copy_from(f, 'restaurants', sep=',', columns=('CAMIS', 'DBA', 'BORO', 'ZIPCODE', 'SCORE', 'GRADE'))
        cur.copy_expert("COPY restaurants(CAMIS, DBA, BORO, ZIPCODE, SCORE, GRADE) FROM STDIN WITH CSV HEADER DELIMITER ','", f)
        # cur.executemany('INSERT INTO restaurants VALUES ')
    conn.commit()
    conn.close()
    
    # Number of rows
    nrows = 0
    # List of properties
    props = []
    return nrows + " rows loaded\nList of properties:" + props 


if __name__ == "__main__":
    print(load_data())
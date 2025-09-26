from database.conncection import get_connection  

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cmd_user = """
            CREATE TABLE IF NOT EXISTS TB_USER
            (
                ID SERIAL PRIMARY KEY,
                NAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL UNIQUE,
                DATE_BIRTH DATE NOT NULL,
                ROLE TEXT NOT NULL,
                PASSWORD_WITH_HASH TEXT NOT NULL
            );
        """
        cursor.execute(cmd_user)

        cmd_customer = """
            CREATE TABLE IF NOT EXISTS TB_CUSTOMER
            (
                ID SERIAL PRIMARY KEY,
                NAME TEXT NOT NULL UNIQUE,
                SECTOR TEXT NOT NULL,
                IS_ACTIVE BOOLEAN NOT NULL
            );
        """
        cursor.execute(cmd_customer)

        cmd_position = """
            CREATE TABLE IF NOT EXISTS TB_POSITION
            (
                ID SERIAL PRIMARY KEY,
                NAME TEXT NOT NULL,
                SENIORITY TEXT NOT NULL,
                DATE_CREATED DATE NOT NULL,
                IS_FINISHED BOOLEAN NOT NULL,
                CUSTOMER_ID INT NOT NULL,
                CONSTRAINT FK_CUSTOMER_POSITION FOREIGN KEY(CUSTOMER_ID) REFERENCES TB_CUSTOMER(ID)
            );
        """
        cursor.execute(cmd_position)

        cmd_technology = """
            CREATE TABLE IF NOT EXISTS TB_TECHNOLOGY
            (
                ID SERIAL PRIMARY KEY,
                NAME TEXT NOT NULL,
                POSITION_ID INT NOT NULL,
                CONSTRAINT FK_POSITION_TECHNOLOGY FOREIGN KEY (POSITION_ID) REFERENCES TB_POSITION(ID)
            );
        """
        cursor.execute(cmd_technology)

        cmd_candidate = """
            CREATE TABLE IF NOT EXISTS TB_CANDIDATE
            (
                ID SERIAL PRIMARY KEY,
                NAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                PHONE TEXT NOT NULL,
                IS_APPROVED BOOLEAN NOT NULL,
                POSITION_ID INT NOT NULL,
                CONSTRAINT FK_CANDIDATE_POSITION FOREIGN KEY (POSITION_ID) REFERENCES TB_POSITION(ID)
            );
        """
        cursor.execute(cmd_candidate)

        conn.commit()  # confirma todas as alterações
    finally:
        cursor.close()
        conn.close()

from models.Position.Position import PositionCreate as Position
from models.Position.Position import TechnologyPositionCreate
from database.conncection import get_connection

def add_position(position:Position):
    sql = """
        INSERT TB_POSITION
        NAME, SENIORITY, DATE_CREATED, IS_FINISHED, CUSTOMER_ID)
        VALUES
        (%s, %s, %s, %s, %s);
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql,(position.name,position.seniority,position.date_created,position.is_finished,position.customer_id))
    conn.commit()
    conn.close()

def edit_position(position:Position, id:int):
    SQL = """
        UPDATE TB_POSITION
        SET NAME = %s, SENIORITY = %s, DATE_CREATED = %s, IS_FINISHED = %s, CUSTOMER_ID = %s
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL, (position.name, position.seniority, position.date_created, position.is_finished, position.customer_id,id))
    conn.commit()
    conn.close()


def delete_position(id:int):
    SQL = """
        DELETE FROM TB_POSITION
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL, (id))
    conn.commit()
    conn.close()


def get_all_position():
    SQL = """
        SELECT * FROM TB_POSITION
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "id":item[0],
                "name":item[1],
                "seniority":item[2],
                "date_created":item[3],
                "is_finished":item[4],
                "customer_id":item[5]
            }
        )

def get_position_by_id(id:int):
    SQL = """
        SELECT * FROM TB_POSITION
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    item = cursor.fetchone()
    if(item):
        return item

def add_technology(tech:TechnologyPositionCreate):
    sql = """
        INSERT INTO TB_TECHNOLOGY 
        (NAME, POSITION_ID)
        VALUES
        (%s,%s)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        sql, (tech.technology, tech.position_id)
    )
    conn.commit()
    conn.close()

def edit_technology(tech:TechnologyPositionCreate,  int:id):
    sql = """
        UPDATE TB_TECHNOLOGY
        SET NAME = %s, POSITION_ID = %s
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        sql, (tech.technology, tech.position_id, id)
    )
    conn.commit()
    conn.close()

def delete_technology(id:int):
    SQL = """
        DELETE FROM TB_TECHNOLOGY
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        SQL,
        (id)
    )

def get_all_technology_by_position():
    SQL = """
        SELECT * FROM TB_TECHNOLOGY
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        SQL
    )
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "id":item[0],
                "Name":item[1],
                "position_id":item[2]
            }
        )
    
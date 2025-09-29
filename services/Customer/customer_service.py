from models.Customer.Customer import Customer,CustomerCreate
from database.conncection import get_connection


def create_customer(customer:CustomerCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO TB_CUSTOMER
        (
            NAME, SECTOR, IS_ACTIVE
        )
        VALUES
        (%s, %s, %s)
    """
    cursor.execute(sql, (customer.name, customer.sector, customer.is_active))
    conn.commit()
    conn.close()

def update_customer(customer:CustomerCreate, id:int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE TB_CUSTOMER
        SET NAME = %s, SECTOR = %s, IS_ACTIVE = %s
        WHERE ID = %s
    """
    cursor.execute(sql, (customer.name, customer.sector, customer.is_active, id))
    conn.commit()
    conn.close()

def delete_customer(id:int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        DELETE FROM TB_CUSTOMER
        WHERE ID = %s
    """
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()

def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        SELECT * FROM TB_CUSTOMER
    """
    cursor.execute(sql)
    list = cursor.fetchall()
    result = []

    for item in list:
        result.append(
            {
                "id":item[0],
                "name":item[1],
                "sector":item[2],
                "is_active":item[3]
            }
        )
    return result


def get_customer_by_id():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM TB_CUSTOMER WHERE ID = %s"
    cursor.execute(sql)
    item = cursor.fetchone()
    return item
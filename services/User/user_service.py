import bcrypt
from models.User.user import User, UserCreate
from database.conncection import get_connection
from typing import List

# Função para gerar hash de senha
def hash_password(pwd: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd.encode("utf-8"), salt)
    return hashed.decode("utf-8")  # Armazenar como string no banco

def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO TB_USER
        (NAME, EMAIL, DATE_BIRTH, PASSWORD_WITH_HASH, ROLE)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql,
        (
            user.name,
            user.email,
            user.date_birth,
            hash_password(user.passwordWithHash),
            user.role
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_user(id: int, user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE TB_USER
        SET NAME = %s, EMAIL = %s, DATE_BIRTH = %s, PASSWORD_WITH_HASH = %s, ROLE = %s
        WHERE ID = %s
    """
    cursor.execute(
        sql,
        (
            user.name,
            user.email,
            user.date_birth,
            hash_password(user.passwordWithHash),
            user.role,
            id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        DELETE FROM TB_USER
        WHERE ID = %s
    """
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM TB_USER"
    cursor.execute(sql)
    users = cursor.fetchall()
    result = []
    for user in users:
        result.append(
            {
                "id":user[0],
                "name":user[1],
                "email":user[2],
                "date_birth":user[3],
                "role":user[4],
                "password":user[5]
            }
        )
    return result




def get_user_by_id(id:int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM TB_USER WHERE ID = %s"
    cursor.execute(sql,(id,))
    user = cursor.fetchone()
    return user
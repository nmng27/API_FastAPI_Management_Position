from models.Candidates.Candidates import CandidateCreate
from database.conncection import get_connection

def add_candidate(candidate:CandidateCreate):
    sql = """
        INSERT INTO TB_CANDIDATE
        (NAME, MAIL, PHONE, AGE, APPROVED, POSITION_ID)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        sql,
        (candidate.name, candidate.mail, candidate.phone, candidate.age, candidate.approved, candidate.position_id),
    )
    

def edit_candidate(candidate:CandidateCreate):
    SQL = """
        UPDATE TB_CANDIDATE
        SET NAME = %s, MAIL = %s, PHONE = %s, AGE = %s, POSITION_ID = %s
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        SQL,
        (candidate.name, candidate.mail, candidate.phone, candidate.age, candidate.position_id,id)
    )

def delete_candidate(id:int):
    SQL = """
        DELETE FROM TB_CANDIDATE
        WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL, id)

def get_all_candidate():
    SQL = """
        SELECT * FROM TB_CANDIDATE
        WHERE POSITION_ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "Id":item[0],
                "Name":item[1],
                "Mail":item[2],
                "Phone":item[3],
                "Age":item[4],
                "Position":item[5]
            }
        )

def candidate_by_id():
    SQL = """
        SELECT * FROM TB_CANDIDATE WHERE ID = %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "Id":item[0],
                "Name":item[1],
                "Mail":item[2],
                "Phone":item[3],
                "Age":item[4],
                "Position":item[5]
            }
        )

def get_candidates_approved():
    SQL = """
        SELECT * FROM TB_CANDIDATE WHERE APPROVED = TRUE
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "Id":item[0],
                "Name":item[1],
                "Mail":item[2],
                "Phone":item[3],
                "Age":item[4],
                "Position":item[5]
            }
        )


def get_candidates_repproved():
    SQL = "SELECT * FROM TB_CANDIDATE WHERE APPROVED = FALSE"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
    list = cursor.fetchall()
    result = []
    for item in list:
        result.append(
            {
                "Id":item[0],
                "Name":item[1],
                "Mail":item[2],
                "Phone":item[3],
                "Age":item[4],
                "Position":item[5]
            }
        )

def approve():
    SQL = "UPDATE TB_CANDIDATE SET APPROVE = TRUE WHERE ID = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)

def reprove():
    SQL = "UPDATE TB_CANDIDATE SET APPROVE = FALSE WHERE ID = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(SQL)
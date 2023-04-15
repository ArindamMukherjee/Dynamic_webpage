from sqlalchemy import create_engine, text
import os

security = os.environ['DB_Coneection_String']
ssl_args = {'ssl': {'ssl_mode': 'VERIFY_IDENTITY'}}
engine = create_engine(security,connect_args=ssl_args)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM job"))
    rows = result.fetchall()
    # print(rows)
    # rows_dict = [dict(rows[0])]
    # print(type(rows_dict))
    column_names = result.keys()  # get column names from the result object
    result_dict = [dict(zip(column_names, row)) for row in rows]  # convert each row tuple to a dictionary

    print(result_dict)
def load_job_from_db():
  with engine.connect() as conn:
    jobs = conn.execute(text("SELECT * FROM job"))
    rows = jobs.fetchall()
    print(rows)
    # rows_dict = [dict(rows[0])]
    # print(type(rows_dict))
    column_names = jobs.keys()  # get column names from the result object
    result_dict = [dict(zip(column_names, row)) for row in rows]  # convert each row tuple to a dictionary
    return result_dict


def load_jobs_from_db(id):
 with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM job WHERE id = :id"),{'id': id})
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      column_names = result.keys()  # get column names from the result object
      result_dict = [dict(zip(column_names, row)) for row in rows]  # convert each row tuple to a dictionary
      return result_dict[0]
def application_to_the_db(job_id,data):
  with engine.connect() as conn:
    query = conn.execute(text("INSERT INTO applications (job_id,full_name, email, linkedin_url, education, work_experience, resume_url,)"))
    conn.execute(query, 
                   job_id=job_id, 
                   full_name=data['full_name'],
                   email=data['email'],
                   linkedin_url=data['linkedin_url'],
                   education=data['education'],
                   work_experience=data['work_experience'],
                   resume_url=data['resume_url'])
    

 
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM job WHERE id = :id"),{'id': id})
#     rows = result.fetchall()
#     if len(rows) == 0:
#       return None
#     else:
#       column_names = result.keys()  # get column names from the result object
#       result_dict = [dict(zip(column_names, row)) for row in rows]  # convert each row tuple to a dictionary
#       return result_dict[0]
    
    

    

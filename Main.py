import os

from dotenv import load_dotenv

from DBHandler import DBHandler

load_dotenv()




def TaskDoneWatch(db_id) -> None:
    results = db_handler.get_done_task_db(db_id)
    for idx in range(len(results)):
        page_id = db_handler.get_page_id(results[idx])
        db_handler.update_task_date(page_id)


db_handler = DBHandler(os.getenv("NOTION_TOKEN"))

TaskDoneWatch(os.getenv("PRIVATE_DB"))
TaskDoneWatch(os.getenv("WORK_DB"))

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pytest

base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / ".env")

password = os.getenv("DB_PASSWORD")

db_connection_string = f"postgresql://postgres:{password}@localhost:5432/QA"
engine = create_engine(db_connection_string)


@pytest.fixture
def unique_student_id():
    import random
    return random.randint(1000000, 9999999)


@pytest.fixture
def unique_subject_id():
    # Аналогично для subject_id
    import random
    return random.randint(1000000, 9999999)


def test_insert_student(unique_student_id, unique_subject_id):
    test_level = "Test Level Insert"
    test_education_form = "Test Form"

    try:
        with engine.begin() as connection:
            insert_sql = text(
                "INSERT INTO student "
                "(user_id, subject_id, level, education_form) "
                "VALUES (:uid, :sid, :lvl, :form)"
            )
            connection.execute(insert_sql, {
                "uid": unique_student_id,
                "sid": unique_subject_id,
                "lvl": test_level,
                "form": test_education_form
            })

            check_sql = text(
                "SELECT * FROM student WHERE user_id = :uid "
                "AND subject_id = :sid"
            )
            result = connection.execute(check_sql, {
                "uid": unique_student_id,
                "sid": unique_subject_id
            }).fetchone()

            assert result is not None, "Студент не был добавлен!"
            assert result.level == test_level, "Уровень не совпадает!"

    finally:
        with engine.begin() as connection:
            connection.execute(
                text("DELETE FROM student WHERE user_id = :uid "
                     "AND subject_id = :sid"),
                {"uid": unique_student_id, "sid": unique_subject_id}
            )


def test_update_student(unique_student_id, unique_subject_id):
    old_level = "Old Level"
    new_level = "New Level"

    try:
        with engine.begin() as connection:
            connection.execute(
                text("INSERT INTO student"
                     "(user_id, subject_id, level, education_form) "
                     "VALUES (:uid, :sid, :lvl, 'group')"),
                {"uid": unique_student_id,
                 "sid": unique_subject_id,
                 "lvl": old_level}
            )

        with engine.begin() as connection:
            update_sql = text(
                "UPDATE student SET level = :new_lvl "
                "WHERE user_id = :uid AND subject_id = :sid"
            )
            result = connection.execute(update_sql, {
                "new_lvl": new_level,
                "uid": unique_student_id,
                "sid": unique_subject_id
            })
            assert result.rowcount == 1, "Не удалось обновить студента!"

            check = connection.execute(
                text("""
                    SELECT level FROM student
                    WHERE user_id = :uid
                    AND subject_id = :sid
                """),
                {"uid": unique_student_id, "sid": unique_subject_id}
            ).scalar()
            assert check == new_level, "Уровень не обновился!"

    finally:
        with engine.begin() as connection:
            connection.execute(
                text("DELETE FROM student WHERE user_id = :uid "
                     "AND subject_id =:sid"),
                {"uid": unique_student_id, "sid": unique_subject_id}
            )


def test_delete_student(unique_student_id, unique_subject_id):
    try:
        with engine.begin() as connection:
            connection.execute(
                text("INSERT INTO student "
                     "(user_id, subject_id, level, education_form) "
                     "VALUES (:uid, :sid, 'Level', 'group')"),
                {"uid": unique_student_id, "sid": unique_subject_id}
            )

        with engine.begin() as connection:
            delete_sql = text(
                "DELETE FROM student WHERE user_id = :uid "
                "AND subject_id = :sid"
            )
            result = connection.execute(delete_sql, {
                "uid": unique_student_id,
                "sid": unique_subject_id
            })
            assert result.rowcount == 1, "Не удалось удалить студента!"

            check = connection.execute(
                text("SELECT * FROM student WHERE user_id = :uid "
                     "AND subject_id = :sid"),
                {"uid": unique_student_id, "sid": unique_subject_id}
            ).fetchone()
            assert check is None, "Студент все еще в базе!"

    finally:
        with engine.begin() as connection:
            connection.execute(
                text("DELETE FROM student WHERE user_id = :uid "
                     "AND subject_id = :sid"),
                {"uid": unique_student_id, "sid": unique_subject_id}
            )

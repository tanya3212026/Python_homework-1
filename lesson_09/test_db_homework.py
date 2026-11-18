import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / ".env")

# Получаем пароль из переменной окружения
password = os.getenv("DB_PASSWORD")

# Собираем строку подключения
db_connection_string = f"postgresql://postgres:{password}@localhost:5432/QA"
engine = create_engine(db_connection_string)


def test_insert_student():
    test_user_id = 999999
    test_subject_id = 999
    test_level = "Test Level"
    test_education_form = "Test Form"

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM student WHERE user_id = :uid "
                 "AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        )
        insert_sql = text(
            "INSERT INTO student (user_id, subject_id, level, education_form) "
            "VALUES (:uid, :sid, :lvl, :form)"
        )
        connection.execute(insert_sql, {
            "uid": test_user_id,
            "sid": test_subject_id,
            "lvl": test_level,
            "form": test_education_form
        })

        check_sql = text(
            "SELECT * FROM student "
            "WHERE user_id = :uid AND subject_id = :sid"
        )
        result = connection.execute(
            check_sql, {"uid": test_user_id, "sid": test_subject_id}
        ).fetchone()

        assert result is not None, "Студент не был добавлен!"
        assert result.level == test_level, "Уровень не совпадает!"

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM student WHERE user_id = :uid "
                 "AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        )


def test_update_student():
    test_user_id = 999998
    test_subject_id = 999
    old_level = "Old Level"
    new_level = "New Level"

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM student WHERE user_id = :uid "
                 "AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        )
        connection.execute(
            text("INSERT INTO student "
                 "(user_id, subject_id, level, education_form) "
                 "VALUES (:uid, :sid, :lvl, 'group')"),
            {"uid": test_user_id, "sid": test_subject_id, "lvl": old_level}
        )

    with engine.begin() as connection:
        update_sql = text(
            "UPDATE student SET level = :new_lvl "
            "WHERE user_id = :uid AND subject_id = :sid"
        )
        result = connection.execute(
            update_sql,
            {"new_lvl": new_level, "uid": test_user_id, "sid": test_subject_id}
        )
        assert result.rowcount == 1, "Не удалось обновить студента!"

        check = connection.execute(
            text("SELECT level FROM student "
                 "WHERE user_id = :uid AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        ).scalar()
        assert check == new_level

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM student WHERE user_id = :uid "
                 "AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        )


def test_delete_student():
    test_user_id = 999997
    test_subject_id = 999

    with engine.begin() as connection:
        connection.execute(
            text("INSERT INTO student "
                 "(user_id, subject_id, level, education_form) "
                 "VALUES (:uid, :sid, 'Level', 'group')"),
            {"uid": test_user_id, "sid": test_subject_id}
        )

    with engine.begin() as connection:
        delete_sql = text(
            "DELETE FROM student WHERE user_id = :uid AND subject_id = :sid"
        )
        result = connection.execute(
            delete_sql, {"uid": test_user_id, "sid": test_subject_id}
        )
        assert result.rowcount == 1, "Не удалось удалить студента!"

        check = connection.execute(
            text("SELECT * FROM student "
                 "WHERE user_id = :uid AND subject_id = :sid"),
            {"uid": test_user_id, "sid": test_subject_id}
        ).fetchone()
        assert check is None, "Студент все еще в базе!"

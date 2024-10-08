from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "division" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "director" VARCHAR(250) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(250) NOT NULL,
    "last_name" VARCHAR(250) NOT NULL,
    "login" VARCHAR(250) NOT NULL,
    "password" VARCHAR(250) NOT NULL,
    "email" VARCHAR(250) NOT NULL,
    "start_vacation" DATE,
    "finish_vacation" DATE,
    "start_business_trip" DATE,
    "finish_business_trip" DATE,
    "division_id" INT REFERENCES "division" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "taskservice" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "employee_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "task_division_id" INT NOT NULL REFERENCES "division" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

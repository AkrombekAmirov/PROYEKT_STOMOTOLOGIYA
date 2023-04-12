# PROYEKT_STOMOTOLOGIYA
private
step 1 create docker images redis CMD RUN "docker run --name my-redis-container -d -p 6379:6379 redis"

step 2 create docker images postgresql CMD RUN "docker run -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin_user -e POSTGRES_DB=symptomatologic -p 5432:5432 -d postgres"

step 3 sudo apt-get update

step 4 sudo apt-get install postgresql-client

step 5 CMD RUN python -m main.migrate migrate 

step 6 psql -h localhost -U admin_user -d symptomatologic

step 7 INSERT INTO "user" (role, first_name, last_name, username, password, address, phone_number, created_date)
VALUES ('admin', 'TestUser', 'User', 'username', 'mypassword', 'New York', '+1234567890', NOW());

step 8 CMD RUN python -m uvicorn main:app --reload

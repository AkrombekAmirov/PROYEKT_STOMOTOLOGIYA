docker run --name my-redis-container -d -p 6379:6379 redis
docker run -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin_user -e POSTGRES_DB=symptomatologic -p 5432:5432 -d postgres
python -m main.migrate migrate
sudo apt-get update
sudo apt-get install postgresql-client
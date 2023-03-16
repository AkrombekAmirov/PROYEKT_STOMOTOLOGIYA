# PROYEKT_STOMOTOLOGIYA
private
create docker images redis CMD RUN "docker run --name my-redis-container -d -p 6379:6379 redis"
create docker images postgresql CMD RUN "docker run -e POSTGRES_PASSWORD=mysecret54321 -e POSTGRES_USER=admin_user -e POSTGRES_DB=symptomatologic -p 5434:5434 -d postgres"
CMD RUN python -m main.migrate migrate 
CMD RUN python -m uvicorn main:app --reload

rpcuser = 'edunuke'
rpcpassword = 'mysupersecretpwd' #DO NOT USED THIS YOU WILL GET ROBBED

build btcserver
> docker build -t bitcoin-server .

for regtest:
> docker run --rm --name bitcoin-server -d -it -p 18443:18443 bitcoin-core -printtoconsole
docker run --rm --name btc-core -it -d -p 18443:18443 -p 5000:5000 -p 9001:9001 btc-core

run waitress:
> waitress-serve --host=127.0.0.1  --port=8000 app:app


build btcvalidator:
> docker build -t btc-validator .

run btc validator:
> docker run --rm --name btc-validator -it -d -p 5000:5000 btc-validator

#-------------

Member Page (login_required: member@example.com / Password1)
Admin Page (roles_required: admin@example.com / Password1)

#-----------
{
    "status": 1,
    "message": "Address key creted",
    "data": {
        "userid": "1",
        "address": "2N5VSQVQ89LCwB9xYjXGhDPArLDiXFraZoj"
    }
}
{
    "status": 1,
    "message": "Address key creted",
    "data": {
        "userid": "2",
        "address": "2N7s8NHxfSTRUJEggxZfv2uzuCKsUoRbzDA"
    }
}
{
    "status": 1,
    "message": "Address key creted",
    "data": {
        "userid": "3",
        "address": "2N8p7zY9LPHZxbzQZoDiXoFdKjqsonyZkX6"
    }
}


#%%%%%
version: '3.5'

services:
  btc-api:
    build: btcapi
    ports:
      - "8000:8000"
      - "9001:9001"
    networks:
      - btcnet

  btc-core:
    build: btcservice
    ports:
      - "9002:9001"
    networks:
      - btcnet

  btc-app:
    build: btcapp
    ports:
      - "8080:5000"

  redis:
    build: redis
    command: ["--appendonly", "yes"]
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

  postgres:
    image: postgres
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: test
      POSTGRES_USER: test
      POSTGRES_DB: test
      
networks:
  btcnet:
    name: btcnet

volumes:
  redis-data:
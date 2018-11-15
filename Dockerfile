FROM ubuntu:latest
RUN apt-get update && apt-get install -y redis-server
ARG NEW_PORT
ENV REDIS_PORT=$NEW_PORT
ARG MEM
ENV MAX_MEMORY $MEM
RUN sed -i "\$amaxmemory $MAX_MEMORY" /etc/redis/redis.conf
CMD ["sh", "-c", "exec redis-server --port \"$REDIS_PORT\""]

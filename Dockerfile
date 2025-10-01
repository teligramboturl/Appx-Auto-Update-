FROM python:3.10-alpine3.16
WORKDIR /app
COPY . .
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt 
CMD [ "python", "plugins" ]

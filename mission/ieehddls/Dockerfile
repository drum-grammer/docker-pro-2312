FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["echo", "hello-wolrd"]
EXPOSE 3000
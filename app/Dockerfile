#Stage 1
FROM node:latest
WORKDIR /app
COPY package*.json .
COPY . .
RUN npm run build
CMD [ "npm", "start" ]
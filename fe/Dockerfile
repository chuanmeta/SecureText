FROM node:24 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

RUN npm run build --prod

#
# FROM nginx:latest
# COPY --from=build /app/dist/fe/browser /usr/share/nginx/html

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]
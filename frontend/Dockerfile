FROM node:19.9.0 as build-stage

WORKDIR /app
COPY package*.json ./
COPY . .

ARG VITE_BASE_URL
ENV VITE_BASE_URL=$VITE_BASE_URL


# CMD ["sudo", "npm", "run", "build"]
RUN npm i
# RUN npm i && npm run build
# RUN npm run build
# CMD ["sudo", "npm", "run", "build"]

FROM nginx:1.22.1 as production-stage
RUN apt-get update
RUN usermod -aG root nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY --from=build-stage /app/src/assets /usr/share/nginx/html/src/assets
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
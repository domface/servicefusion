FROM nginx
COPY nginx.development.conf /etc/nginx/nginx.conf
COPY ./dist /usr/share/nginx/html/
RUN mkdir /www/
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

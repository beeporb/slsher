FROM node:latest as build

WORKDIR /src/build

COPY ./package.json /src/build/package.json
RUN yarn

COPY . /src/build/

RUN yarn build

FROM caddy:latest

WORKDIR /var/www

COPY --from=build /src/build/dist /var/www

ENTRYPOINT [ "caddy", "file-server", "--listen", ":80", "--root", "/var/www"  ]
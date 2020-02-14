# base image
FROM node:13

ARG API_URL
ENV REACT_APP_API_URL $API_URL

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
RUN npm install --silent
RUN npm install react-scripts@3.3.0 -g --silent

# start app
CMD ["npm", "start"]
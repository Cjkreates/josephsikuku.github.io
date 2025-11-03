# Use official Nginx image as base
FROM nginx:alpine

# Copy your website files to Nginx directory
COPY . /usr/share/nginx/html

# Expose port 80 (default web port)
EXPOSE 80

# Start Nginx when container runs
CMD ["nginx", "-g", "daemon off;"]
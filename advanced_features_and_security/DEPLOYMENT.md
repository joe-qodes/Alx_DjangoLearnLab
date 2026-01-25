# HTTPS Deployment Configuration

This Django application is configured to enforce HTTPS for all incoming requests.

## Web Server Configuration (Example: Nginx)

An SSL/TLS certificate must be installed on the server. This can be done using
Let's Encrypt or a commercial certificate authority.

Example Nginx configuration:

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

## Notes
- HTTP traffic is permanently redirected to HTTPS.
- SSL certificates must be renewed periodically.

FROM caddy:2.3.0-builder-alpine AS builder

RUN xcaddy build \
				--with github.com/caddy-dns/cloudflare@latest \
				--with github.com/greenpau/caddy-auth-portal \
				--with github.com/greenpau/caddy-auth-jwt

FROM caddy:2.3.0-alpine

COPY --from=builder /usr/bin/caddy /usr/bin/caddy

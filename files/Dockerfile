FROM caddy:2.5.1-builder-alpine AS builder

RUN xcaddy build \
				--with github.com/caddy-dns/cloudflare@latest

FROM caddy:2.3.0-alpine

COPY --from=builder /usr/bin/caddy /usr/bin/caddy

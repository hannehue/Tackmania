FROM golang:1.21 as builder

# Set CGO_ENABLED to 0 to avoid linking with C libraries
# this is required to run the binary in a scratch container
ENV CGO_ENABLED=0

RUN mkdir /build
WORKDIR /build
COPY . .
RUN go mod download \
    && go mod verify \
    && go build -o app

FROM scratch as runner
COPY --from=builder /build/app /app
ENTRYPOINT ["/app"]
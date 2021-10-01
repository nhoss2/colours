from colours import webapp

if __name__ == '__main__':
    import waitress

    host = "0.0.0.0"
    port = 8080
    print(f'running server {host}:{port}')

    waitress.serve(
        webapp,
        host=host,
        port=port,
    )

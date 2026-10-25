def get_cache():
    return redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379,
                       socket_connect_timeout=2, decode_responses=True)


@app.route("/health")
def health():
    return jsonify(status="ok", service="shopease-api",
                   version=os.getenv("APP_VERSION", "dev"))
...

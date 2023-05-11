def stress_cpu():
    # Start stress_cpu.py in a separate process
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'Started stressing the CPU.', 200



@app.get("/")
def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({'private_ip': private_ip})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

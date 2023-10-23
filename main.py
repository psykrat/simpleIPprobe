from flask import Flask, request, jsonify
from ipwhois import IPWhois

app = Flask(__name__)

@app.route('/lookup-ip', methods=['POST'])
def lookup_ip():
    try:
        ip = request.json.get('ip')
        if not ip:
            return jsonify({"error": "IP address not provided"}), 400
        
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For local testing
if __name__ == "__main__":
    app.run(debug=True)

from ipwhois import IPWhois

def lookup_ip(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    request_json = request.get_json(silent=True)
    if not request_json or 'ip' not in request_json:
        return 'IP address not provided in the request body', 400

    ip = request_json['ip']

    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        return result
    except Exception as e:
        return f"Error: {str(e)}", 500

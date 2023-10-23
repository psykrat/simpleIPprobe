# simpleIPprobe

This script is for a Google Cloud Function that allows users to look up information about a given IP address using the `ipwhois` library. This can be used in existing automation when logging traffic for systems to detect potentially malicious traffic.

## Features

- Accepts an IP address via a POST request.
- Retrieves ownership and other related details about the IP address.
- Returns the information in a JSON format.

## Prerequisites

- Python 3.x
- Google Cloud SDK (if deploying to Google Cloud Functions)

## Dependencies

The required dependencies are:

- Flask
- ipwhois

You can install these using:

```bash
pip install Flask ipwhois
```

## Local Testing

1. Navigate to the directory containing the script.

2. Run the script:

```bash
python main.py
```

3. Send a POST request with the IP address:

```bash
curl -X POST http://127.0.0.1:5000/lookup-ip -H "Content-Type: application/json" -d '{"ip":"8.8.8.8"}'
```

## Deployment to Google Cloud Functions

1. Ensure you have the Google Cloud SDK installed and are authenticated.

2. Deploy the function:

```bash
gcloud functions deploy lookup_ip \
   --runtime python310 \
   --trigger-http \
   --allow-unauthenticated \
   --entry-point lookup_ip \
   --source=.
```

(Note: Omit the `--allow-unauthenticated` flag if you want to secure your function.)

3. After deployment, Google Cloud Functions will provide a URL endpoint. Use this URL to send POST requests.

## Usage

Send a POST request with a JSON payload containing the IP address you want to look up:

```json
{
    "ip": "8.8.8.8"
}
```

---

:lock_with_ink_pen: by psykrat

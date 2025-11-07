import os
import requests
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# Setup Flask app with static and template folders
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '..', 'public'), static_url_path='')
CORS(app)

DUB_API_KEY = os.getenv('DUB_API_KEY')
DUB_API_URL = 'https://api.dub.co/links'


@app.route('/')
def index():
    """Serve the main index.html file"""
    return send_file(os.path.join(app.static_folder, 'index.html'))


@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """
    Endpoint to shorten a URL using the Dub API
    
    Expected JSON payload:
    {
        "url": "https://example.com/very/long/url",
        "custom_slug": "optional-slug" (optional)
    }
    """
    try:
        data = request.json
        url = data.get('url')
        custom_slug = data.get('custom_slug', '')
        
        # Validation
        if not url:
            return jsonify({
                'success': False,
                'error': 'URL is required'
            }), 400
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        if not DUB_API_KEY:
            return jsonify({
                'success': False,
                'error': 'DUB_API_KEY is not configured'
            }), 500
        
        # Prepare request to Dub API
        headers = {
            'Authorization': f'Bearer {DUB_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'url': url,
        }
        
        # Add custom slug if provided
        if custom_slug:
            payload['slug'] = custom_slug
        
        # Call Dub API
        response = requests.post(DUB_API_URL, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            result = response.json()
            return jsonify({
                'success': True,
                'original_url': url,
                'shortened_url': result.get('shortLink') or f"https://dub.co/{result.get('slug')}",
                'slug': result.get('slug'),
                'qr_code': result.get('qrCode')
            }), 200
        else:
            error_data = response.json() if response.text else {}
            return jsonify({
                'success': False,
                'error': error_data.get('message') or 'Failed to shorten URL',
                'details': error_data
            }), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'API request failed: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'api_key_configured': bool(DUB_API_KEY)
    }), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)


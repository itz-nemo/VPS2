<img width="2940" height="1670" alt="CleanShot 2025-11-07 at 15 59 18@2x" src="https://github.com/user-attachments/assets/d001a9d2-d8bd-40b6-98b0-59a7223991d8" />
# URL Shortener - Vercel Python App

A modern web application for shortening URLs using the Dub API. Built with Flask, deployed on Vercel.

## Features

✨ **Modern UI** - Beautiful, responsive interface with gradient design  
🔗 **URL Shortening** - Instantly shorten long URLs  
🏷️ **Custom Slugs** - Create custom shortened links  
📱 **QR Codes** - Auto-generated QR codes for shortened URLs  
📋 **One-Click Copy** - Easy copy-to-clipboard functionality  
🚀 **Vercel Ready** - Deploy in seconds  

## Getting Started

### Prerequisites

- Python 3.8+
- Dub API Key (get one at [dub.co](https://dub.co))

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd url-shortener
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your Dub API key
```

5. **Run locally**
```bash
python api/index.py
```

Visit `http://localhost:5000` in your browser.

## Deployment to Vercel

### Option 1: Using Vercel CLI

1. **Install Vercel CLI**
```bash
npm i -g vercel
```

2. **Deploy**
```bash
vercel
```

3. **Set environment variables**
   - During deployment, add `DUB_API_KEY` environment variable
   - Or add it later in Vercel dashboard under Settings > Environment Variables

### Option 2: Connect GitHub Repository

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Add `DUB_API_KEY` to environment variables
6. Click "Deploy"

### Option 3: Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Choose "Other" for non-git projects
4. Upload your project files
5. Add environment variables
6. Deploy

## API Endpoints

### POST `/api/shorten`

Shortens a URL using the Dub API.

**Request Body:**
```json
{
  "url": "https://example.com/very/long/url",
  "custom_slug": "optional-slug"
}
```

**Response:**
```json
{
  "success": true,
  "original_url": "https://example.com/very/long/url",
  "shortened_url": "https://dub.co/abc123",
  "slug": "abc123",
  "qr_code": "https://api.dub.co/qr?slug=abc123"
}
```

### GET `/api/health`

Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "api_key_configured": true
}
```

## Getting a Dub API Key

1. Visit [dub.co](https://dub.co)
2. Sign up or log in
3. Go to [Dashboard Settings](https://dub.co/dashboard/settings/tokens)
4. Click "Create Token"
5. Copy your API key
6. Add it to your `.env` file or Vercel environment variables

## Project Structure

```
.
├── api/
│   └── index.py              # Flask backend
├── public/
│   └── index.html            # Frontend UI
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
├── .env.example             # Environment variables template
└── README.md                # This file
```

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **API**: Dub API
- **Deployment**: Vercel
- **Styling**: Modern CSS with gradients and animations

## Troubleshooting

### "DUB_API_KEY is not configured"
- Make sure you've added the `DUB_API_KEY` environment variable
- For local development, create a `.env` file with your key
- For Vercel, add it in Settings > Environment Variables

### CORS errors
- CORS is enabled for all origins in the Flask app
- If you experience issues, check your browser console for specific errors

### 404 errors on Vercel
- Make sure `vercel.json` routes are correct
- Verify that `api/index.py` and `public/index.html` exist
- Redeploy after making changes

## Performance Tips

- Custom slugs are faster than auto-generated ones
- QR codes are generated server-side by Dub
- Results are cached at the edge by Vercel

## Security

- Never commit `.env` files with real API keys
- Always use environment variables in production
- The API key is only used server-side, never exposed to clients

## License

MIT

## Support

For issues with:
- **This app**: Check GitHub Issues
- **Dub API**: Visit [dub.co/docs](https://dub.co/docs)
- **Vercel**: Visit [vercel.com/docs](https://vercel.com/docs)

---

Made with ❤️ using Vercel Python Runtime


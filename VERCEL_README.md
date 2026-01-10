# Deployment Configuration (Vercel)

To deploy the dashboard to Vercel, please configure the project strictly as follows:

## Project Settings
*   **Root Directory:** `dashboard`
    *   *Note: In Vercel Project Settings > General > Root Directory, click "Edit" and select the `dashboard` folder.*

## Build Settings
*   **Ignored Build Step:** `git diff --quiet HEAD^ HEAD -- .`
    *   *Note: This command ensures Vercel only rebuilds if the `dashboard` folder has changed. Enter this in the "Ignored Build Step" field in Project Settings > Git.*

## Environment Variables
*   Ensure the `VITE_API_URL` environment variable is set if the backend is hosted separately. For this Dockerized pipeline, the backend runs alongside the frontend in tests, but for Production Vercel deployment, you likely need a separate backend URL.

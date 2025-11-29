# Deployment Guide for Render

## Prerequisites
- A GitHub account
- A Render account (sign up at https://render.com)
- Your code pushed to a GitHub repository

## Step-by-Step Deployment

### 1. Push Your Code to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 2. Create a New Web Service on Render
1. Log in to your Render dashboard
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Select the repository containing this project

### 3. Configure Your Web Service

**Basic Settings:**
- **Name**: `hospital-management-system` (or your preferred name)
- **Region**: Choose the closest to your users
- **Branch**: `main`
- **Root Directory**: Leave blank (unless your app is in a subdirectory)
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn app:app`

**Instance Type:**
- Select "Free" for testing (or paid plans for production)

### 4. Set Environment Variables
In the Render dashboard, add these environment variables:

- **SECRET_KEY**: Generate a strong random key (e.g., use `python -c "import secrets; print(secrets.token_hex(32))"`)
- **DATABASE_URL**: Render will auto-provide this if you add a PostgreSQL database (optional for SQLite)

### 5. Deploy
1. Click "Create Web Service"
2. Render will automatically:
   - Install dependencies from `requirements.txt`
   - Run the `build.sh` script
   - Start your application with Gunicorn

### 6. Access Your Application
- Once deployed, Render provides a URL like: `https://your-app-name.onrender.com`
- Default admin credentials:
  - **Email**: admin@hospital.com
  - **Password**: admin123
  - ⚠️ **IMPORTANT**: Change the admin password after first login!

## Optional: Add PostgreSQL Database (Recommended for Production)

SQLite works for testing, but PostgreSQL is recommended for production:

1. In Render dashboard, click "New +" and select "PostgreSQL"
2. Create a new PostgreSQL database
3. Copy the "Internal Database URL"
4. Add it as `DATABASE_URL` environment variable in your web service
5. Redeploy your application

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure `build.sh` has proper permissions
- Verify all dependencies are in `requirements.txt`

### Application Won't Start
- Check the deploy logs
- Verify the start command is correct: `gunicorn app:app`
- Ensure port binding is correct (Render handles this automatically)

### Database Issues
- If using SQLite, the database will be ephemeral (resets on each deploy)
- For persistent data, use PostgreSQL
- Check that `init_db()` runs successfully in build logs

### Static Files Not Loading
- Ensure your `static/` folder is committed to Git
- Check file paths are relative, not absolute

## Important Security Notes

1. **Change Default Credentials**: Update admin password immediately
2. **Secret Key**: Use a strong random secret key in production
3. **Database**: Use PostgreSQL for production, not SQLite
4. **HTTPS**: Render provides free SSL certificates automatically
5. **Environment Variables**: Never commit sensitive data to Git

## Maintenance

### Updating Your Application
1. Push changes to GitHub
2. Render will automatically redeploy
3. Or manually trigger deploy from Render dashboard

### Monitoring
- Check logs in Render dashboard
- Set up alerts for errors
- Monitor resource usage

## Support
- Render Documentation: https://render.com/docs
- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/

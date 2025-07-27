# 💜 Purple Vibes Backend API

The **Purple Vibes API** is a robust RESTful API built using **Django** and the **Django REST Framework (DRF)**. It powers the backend of a dynamic content-sharing and social storytelling platform, enabling features like user authentication, posting stories, following other users, liking content, and leaving feedback. Designed for scalability and flexibility, this backend integrates seamlessly with a React-based frontend.

---

## 🚀 Live Site

Access the deployed API here:
👉 **[https://purple-vibes-backend-1acc8e595a6f.herokuapp.com/](https://purple-vibes-backend-1acc8e595a6f.herokuapp.com/)**

> 📝 **Note**: This README is for the back-end API only. For front-end documentation, visit the [Purple Vibes Front-End Repo](https://github.com/sharanraj16/purple-vibes-frontend).

---

## 📚 Table of Contents

* [📖 Project Overview](#-project-overview)
* [🌀 Agile Methodology](#-agile-methodology)
* [🧠 Wireframes](#-wireframes)
* [🛠 Technologies Used](#-technologies-used)
* [🗃 Database](#-database)
* [✅ Testing](#-testing)
* [🚢 Deployment](#-deployment)
* [🙌 Credits](#-credits)

---

## 📖 Project Overview

**Purple Vibes** is a community-driven platform focused on storytelling and connection. The API supports the following core features:

* 🧑‍💻 **User Registration & JWT Authentication**
* 📝 **Post Creation & Management** (CRUD functionality)
* ❤️ **Like & Follow Systems** for engagement
* 💬 **Feedback/Comment System**
* 🖼 **Media Uploads** via **Cloudinary**
* 🔒 **Secure** and **Scalable** architecture using PostgreSQL

This API is optimized for performance and designed with modularity in mind, enabling seamless interaction with the front-end built in React.

---

## 🌀 Agile Methodology

Development followed an **Agile** workflow to promote:

* Continuous integration of feedback
* Iterative development
* Visibility through regular updates and reviews


![Purple Vibes UI](images/5.png)

![Purple Vibes UI](images/6.png)

![Purple Vibes UI](images/7.png)
📌

## 🧠 Wireframes

Visual blueprints were created during the planning phase to guide UI/UX design and endpoint structure.

> *(Include images or links to wireframes if available)*

---

## 🛠 Technologies Used

| Tool/Library              | Purpose                                                            |
| ------------------------- | ------------------------------------------------------------------ |
| **Django**                | Core backend framework                                             |
| **Django REST Framework** | Simplifies API development with serializers, viewsets, and routers |
| **PostgreSQL**            | Relational database for scalable and secure data storage           |
| **Cloudinary**            | Image and media upload/management                                  |
| **JWT Authentication**    | Secure token-based authentication                                  |
| **Gunicorn**              | WSGI HTTP server for deploying Django apps                         |
| **Heroku**                | Cloud platform for deployment                                      |

---

## 🗃 Database

The API uses **PostgreSQL**, hosted via **Code Institute's provisioned database service**, to store data for:

* User profiles
* Stories/posts
* Likes and follows
* Comments and feedback

Django’s ORM (Object-Relational Mapping) ensures data integrity and model relationships.

---

## ✅ Testing

Comprehensive testing was performed to ensure API reliability and robustness.

🔗 See full testing details here: [TESTING.md](TESTING.md)

Types of tests include:

* ✅ Unit Tests for individual components
* 🔄 Integration Tests for multi-part workflows
* 🔐 Authentication and authorization checks
* 🧪 Manual front-end integration validation

---

## 🚢 Deployment

The app is deployed on **Heroku** with the following setup:

* **Gunicorn** used as the WSGI server
* **Cloudinary** used for media file management
* **PostgreSQL** provisioned via Heroku or Code Institute’s platform
* Environment variables managed securely

🧭 Full instructions: [DEPLOYMENT.md](DEPLOYMENT.md)


* 🔙 [⬅ Back to README](README.md)
* 🔙 [⬅ Back to Testing](TESTING.md)

# 🚀 Deployment Guide – Purple Vibes Backend API

This guide explains how the **Purple Vibes Backend API** was deployed using **Heroku**, with a PostgreSQL database from **Code Institute** and media storage powered by **Cloudinary**. These instructions also assume you're using Django and Django REST Framework and that your code is ready for production.

---

## 🌐 Live Deployment

The live API is deployed here:
🔗 [https://purple-vibes-backend-1acc8e595a6f.herokuapp.com/](https://purple-vibes-backend-1acc8e595a6f.herokuapp.com/)

---

## ✅ Prerequisites Before Deployment

Make sure you have the following setup:

### 🗂️ Required Files

* ✅ `settings.py` configured for production
* ✅ `requirements.txt` generated with all necessary dependencies (`pip freeze > requirements.txt`)
* ✅ `Procfile` created with this line:

  ```bash
  web: gunicorn <project_name>.wsgi
  ```
* ✅ `.gitignore` file includes `env.py` and other sensitive files
* ✅ Static files are collected and ready for production (`python manage.py collectstatic`)
* ✅ GitHub repository connected and pushed

---

## 🧰 PostgreSQL Database (Code Institute)

To obtain a free PostgreSQL database via Code Institute:

1. Log in to the [Code Institute LMS](https://learn.codeinstitute.net/).
2. Navigate to the **PostgreSQL** section.
3. Submit your email address.
4. A unique PostgreSQL database URL will be emailed to you.

> ⚠️ Note: This feature is only available to Code Institute students.

---

## 🚀 Heroku Deployment Steps

### 🔧 Step 1: Create the Heroku App

1. Go to [Heroku Dashboard](https://dashboard.heroku.com/)
2. Click on **"New" → "Create new app"**
3. Enter your app name (e.g., `purple-vibes-backend`)
4. Choose a region (usually Europe or US)
5. Click **“Create app”**

---

### 🔑 Step 2: Set Up Config Vars

1. Go to your Heroku app dashboard.
2. Click the **"Settings"** tab.
3. Click **"Reveal Config Vars"** and add the following:

| Config Key              | Value Description                                                        |
| ----------------------- | ------------------------------------------------------------------------ |
| `DATABASE_URL`          | The PostgreSQL URL sent to your email from Code Institute                |
| `CLOUDINARY_URL`        | Get from your Cloudinary dashboard or your `env.py` (no quotation marks) |
| `SECRET_KEY`            | A brand new secret key, different from the development one               |
| `DISABLE_COLLECTSTATIC` | Set this to `1` to prevent collectstatic errors during first deploy      |

> 💡 You can generate a secret key using this in Python:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

### 🔗 Step 3: Connect to GitHub

1. Go to the **"Deploy"** tab.
2. Under **Deployment Method**, select **GitHub**.
3. Search for your GitHub repo (e.g., `purple-vibes-backend-api`) and click **Connect**.

---

### 🚨 Step 4: Deploy the App

1. In the **Manual Deploy** section, choose your main branch (usually `main` or `master`).
2. Click **"Deploy Branch"**
3. Wait for the deployment to finish. Look out for a "Build Succeeded" message.
4. Click **"Open app"** to view your live backend.

---

### 🔁 Optional: Enable Automatic Deploys

* Turn on **Automatic Deploys** from the selected branch.
* This ensures Heroku redeploys your app whenever you push updates to GitHub.

---

## 🧪 Post-Deployment Checks

After your app is live, make sure to:

* ✅ Test all API endpoints using [Postman](https://www.postman.com/)
* ✅ Check JWT authentication (login, signup, token verification)
* ✅ Verify media uploads are working via Cloudinary
* ✅ Confirm the database is saving stories, likes, comments, etc.
* ✅ Run admin panel checks at `/admin` if staff access is configured

---

## 🐞 Common Issues & Fixes

| Problem                              | Solution                                                              |
| ------------------------------------ | --------------------------------------------------------------------- |
| Static files error during deployment | Add `DISABLE_COLLECTSTATIC=1` to Config Vars                          |
| Database errors or no connection     | Double-check your `DATABASE_URL` and ensure `dj_database_url` is used |
| App crashes on load                  | Check the Heroku build logs (`More → View Logs`)                      |
| Secret key warning in production     | Make sure `DEBUG = False` and you’re using a new secret key           |
| Media not uploading                  | Confirm `CLOUDINARY_URL` is correct and account is active             |

---

## 📦 Example Config (in Heroku)

Here’s a quick example of what your **Heroku Config Vars** might look like:

```
DATABASE_URL=postgres://abcd1234:password@host:5432/dbname
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
SECRET_KEY=sk_@1k2!v$%2abcd3fghij4klmnop5qrstuv
DISABLE_COLLECTSTATIC=1
```


---

## 🙌 Credits

* Based on and inspired by the **Code Institute DRF API walkthrough**
* Special thanks to **Code Institute**, mentors, and reviewers
* Assets, icons, and libraries from open-source communities

---


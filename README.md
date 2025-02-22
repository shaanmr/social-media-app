📌 Social Media App

A simple social media application built using Django, HTML, CSS, and JavaScript. This application allows users to register, log in, create posts, and manage their profile.

📌 Features
✔️ User Registration & Authentication  
✔️ Create, Edit, and Delete Posts  
✔️ View All User Posts on Homepage  
✔️ User-Specific Profile Page  
✔️ Responsive Design with Bootstrap  
✔️ Secure Logout  
✔️ Password Reset & Change Functionality  

---

🛠️ Installation & Setup
Follow these steps to set up the project locally.

1. Clone the Repository:

git clone https://github.com/shaanmr/social-media-app.git
cd social-media-app


2. Create a Virtual Environment (Recommended)

python -m venv venv
source venv/Scripts/activate  # For Windows


3. Install Dependencies

pip install -r requirements.txt


4. Apply Migrations & Create Database

python manage.py makemigrations
python manage.py migrate


5. Create Superuser (Optional)

python manage.py createsuperuser

Use:-

Username: admin
Password: admin123

6. Run the Server

python manage.py runserver

Go To: http://127.0.0.1:8000/

📌 Entity Relationship Diagram (ERD)
This diagram represents the database structure.
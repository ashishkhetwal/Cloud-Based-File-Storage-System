# Cloud File Storage System using AWS
A Flask-based web application that allows users to upload files which are stored in AWS S3. The backend is hosted on an EC2 instance.
## Technologies Used
- Python
- Flask
- boto3
- AWS EC2
- AWS S3
- ## Prerequisites:
- Python 3
- AWS account
- AWS S3 bucket
- EC2 instance
- Git
## Deployment Steps
# Connect to EC2 instance
ssh -i your-key.pem ec2-user@your-ec2-public-ip

# Update packages
sudo yum update -y

# Install pip
sudo yum install python3-pip -y

# Install dependencies
pip3 install Flask boto3

# Create project directory
mkdir file_storage_app
cd file_storage_app

# Create application file
nano app.py

# Run the application
python3 app.py

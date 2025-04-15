
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import boto3
import psycopg2
import os

app = Flask(__name__)
api = Api(app)

# Configure AWS S3
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_KEY"
S3_BUCKET = "YOUR_BUCKET_NAME"

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

# Configure Database
DB_HOST = "YOUR_RDS_ENDPOINT"
DB_NAME = "file_conversion_db"
DB_USER = "admin"
DB_PASS = "yourpassword"

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

# JWT Config
app.config["JWT_SECRET_KEY"] = "supersecret"
jwt = JWTManager(app)

class FileUpload(Resource):
    @jwt_required()
    def post(self):
        file = request.files['file']
        filename = file.filename

        s3.upload_fileobj(file, S3_BUCKET, filename)

        return jsonify({"message": "File uploaded successfully!", "file_url": f"https://{S3_BUCKET}.s3.amazonaws.com/{filename}"})

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if username == "admin" and password == "password":
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        return jsonify({"message": "Invalid credentials"}), 401

api.add_resource(UserLogin, "/login")
api.add_resource(FileUpload, "/upload")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import boto3
import psycopg2
import os

app = Flask(__name__)
api = Api(app)

# Configure AWS S3
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_KEY"
S3_BUCKET = "YOUR_BUCKET_NAME"

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

# Configure Database
DB_HOST = "YOUR_RDS_ENDPOINT"
DB_NAME = "file_conversion_db"
DB_USER = "admin"
DB_PASS = "yourpassword"

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

# JWT Config
app.config["JWT_SECRET_KEY"] = "supersecret"
jwt = JWTManager(app)

class FileUpload(Resource):
    @jwt_required()
    def post(self):
        file = request.files['file']
        filename = file.filename

        s3.upload_fileobj(file, S3_BUCKET, filename)

        return jsonify({"message": "File uploaded successfully!", "file_url": f"https://{S3_BUCKET}.s3.amazonaws.com/{filename}"})

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if username == "admin" and password == "password":
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        return jsonify({"message": "Invalid credentials"}), 401

api.add_resource(UserLogin, "/login")
api.add_resource(FileUpload, "/upload")

if __name__ == "__main__":
    app.run(debug=True)


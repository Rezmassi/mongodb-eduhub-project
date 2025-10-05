EduHub MongoDB Project README

This repository contains the full implementation and optimization of a non-relational database for the EduHub online learning platform, using MongoDB as the core data store.

The project demonstrates proficiency in MongoDB schema design, CRUD operations, the Aggregation Framework for business intelligence, and performance optimization through strategic indexing.

🛠️ Technology Stack
Component	Description
Database	MongoDB
Driver	PyMongo
Environment	Python 3.x, Jupyter Notebook
Tools	Git/GitHub

Export to Sheets
📂 Repository Structure
The project is organized into the following key files and directories:

File/Directory	Purpose
eduhub_mongodb_project.ipynb	The primary project notebook detailing all steps: setup, data generation, CRUD, aggregation, and optimization.
eduhub_queries.py	Production-ready Python file containing reusable CRUD and Aggregation functions.
schema_validation.json	JSON document defining the schema validation rules applied to all collections.
sample_data.json	JSON export containing sample data for all six collections.
performance_analysis.md	Document analyzing initial query performance, indexing strategy, and final optimized results.
docs/presentation.pptx	Final project summary and analysis.

Export to Sheets
▶️ Getting Started
To run this project, you must have MongoDB installed locally and accessible on the default port.

Prerequisites
MongoDB: Ensure your MongoDB server is running on mongodb://localhost:27017/.

Python: Python 3.x installed.

Dependencies: Install the required Python packages:

Bash

pip install pymongo jupyter
Running the Project
Start MongoDB: Ensure your MongoDB daemon is running.

Execute the Notebook: Open and run all cells in the eduhub_mongodb_project.ipynb notebook sequentially. This will:

Drop and recreate the eduhub_db database.

Create all 6 collections with schema validation.

Insert all sample data.

Execute all CRUD and aggregation queries.

Apply necessary indexes and perform the final performance analysis.

✨ Key Project Achievements
The project successfully models the platform's data and provides critical functionality:

1. Schema Design and Validation (Task 1 & 2)
Data Model: Implemented a non-normalized model across six core collections: users, courses, enrollments, lessons, assignments, and submissions.

Schema Validation: Applied JSON Schema Validation to the users collection to enforce data integrity (e.g., verifying email format and restricting the role to student or instructor).

2. Advanced Aggregation (Task 4)
Two complex aggregation pipelines were developed to extract high-value business insights:

Monthly Enrollment Trends: Analyzes growth over time by grouping and counting enrollments using date operators.

Course Popularity Statistics: Utilizes the $lookup operator to join the enrollments collection with the courses collection to determine the most popular course titles.

3. Performance Optimization (Task 5)
The most significant achievement was optimizing query times, which is essential for a scalable application.
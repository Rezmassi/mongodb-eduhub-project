# EduHub MongoDB Project

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-4.4+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains the full implementation and optimization of a non-relational database for **EduHub**, an online learning platform, using **MongoDB** as the core data store. The project demonstrates proficiency in MongoDB schema design, CRUD operations, the Aggregation Framework for business intelligence, and performance optimization through strategic indexing.

## 📖 Project Overview

EduHub is a hypothetical online learning platform that connects students and instructors through courses, lessons, and assignments. This project models the platform's data using a non-relational MongoDB database, implementing robust data management and analytics features to support scalability and business insights. The project was developed as a capstone to showcase advanced MongoDB skills, including schema validation, complex aggregations, and query optimization.

## 🛠️ Technology Stack

| Component   | Description                     |
|-------------|---------------------------------|
| Database    | MongoDB (v4.4 or later)        |
| Driver      | PyMongo                        |
| Environment | Python 3.x, Jupyter Notebook   |
| Tools       | Git, GitHub                    |

## 📂 Repository Structure

The project is organized into the following key files and directories:

| File/Directory                | Purpose                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| `eduhub_mongodb_project.ipynb` | Primary project notebook detailing setup, data generation, CRUD, aggregation, and optimization. |
| `eduhub_queries.py`           | Production-ready Python file containing reusable CRUD and Aggregation functions. |
| `schema_validation.json`      | JSON document defining schema validation rules for all collections.      |
| `sample_data.json`            | JSON export containing sample data for all six collections.              |
| `performance_analysis.md`     | Document analyzing initial query performance, indexing strategy, and optimized results. |
| `docs/presentation.pptx`      | Final project summary and analysis presentation.                         |
| `docs/schema_diagram.png`     | Diagram of the MongoDB schema design (added for visualization).          |

## ▶️ Getting Started

To run this project, you need MongoDB installed locally and accessible on the default port.

### Prerequisites

- **MongoDB**: Install MongoDB Community Edition (v4.4 or later) and ensure the MongoDB server is running on `mongodb://localhost:27017/`. Follow the [official MongoDB installation guide](https://www.mongodb.com/docs/manual/installation/) for your operating system.
- **Python**: Install Python 3.8 or later from [python.org](https://www.python.org/downloads/).
- **Dependencies**: Install required Python packages using pip:
  ```bash
  pip install pymongo jupyter
  
  ### Running the Project

1.  **Start MongoDB:** Ensure your MongoDB daemon is running.
2.  **Execute the Notebook:** Open and run all cells in the `eduhub_mongodb_project.ipynb` notebook sequentially. This process includes database setup, data insertion, execution of all queries, and performance analysis.

***

## ✨ Key Project Achievements

The project successfully models the platform's data and provides critical functionality:

### 1. Schema Design and Validation (Task 1 & 2)

* **Data Model:** Implemented a model across six core collections: `users`, `courses`, `enrollments`, `lessons`, `assignments`, and `submissions`.
* **Schema Validation:** Applied **JSON Schema Validation** to the `users` collection to enforce data integrity (e.g., verifying `email` format and restricting the `role` to `student` or `instructor`).

### 2. Advanced Aggregation (Task 4)

Two complex aggregation pipelines were developed to extract high-value business insights:

* **Monthly Enrollment Trends:** Analyzes growth over time by grouping and counting enrollments using date operators.
* **Course Popularity Statistics:** Utilizes the **`$lookup`** operator to join the `enrollments` collection with the `courses` collection to determine the most popular course titles.

### 3. Performance Optimization (Task 5)

The project achieved significant optimization by strategically implementing indexes

### 4. Text Search and Indexing (Bonus Challenge)

* Implemented robust **full-text search** on `courses` by creating a weighted text index on the specific fields.

### 5. Error Handling (Task 6)

* **Robust Query Execution:** Implemented Python `try...except` blocks around database operations to handle potential `PyMongoError` exceptions.
* **Unique Constraints:** Handled potential `DuplicateKeyError` exceptions when attempting to insert documents with non-unique IDs, ensuring the application doesn't crash on constraint violations.
* **Safe Index Management:** Ensured index creation and deletion operations included error handling to prevent runtime issues if an index did not exist or could not be created.

***

## ✅ Conclusion

This project successfully established a highly functional and scalable MongoDB backend for the EduHub platform. By employing **schema validation** for data integrity, leveraging the **Aggregation Framework**, and executing **indexing**, the database is ready to handle both high-volume queries and complex analytical requests with high performance.





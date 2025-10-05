# EduHub MongoDB Project README

This repository contains the full implementation and optimization of a non-relational database for the EduHub online learning platform, using MongoDB as the core data store.

The project demonstrates proficiency in MongoDB schema design, CRUD operations, the Aggregation Framework for business intelligence, and performance optimization through strategic indexing.

## 🛠️ Technology Stack

| Component   | Description                     |
|-------------|---------------------------------|
| Database    | MongoDB                        |
| Driver      | PyMongo                        |
| Environment | Python 3.x, Jupyter Notebook   |
| Tools       | Git/GitHub                     |

## 📂 Repository Structure

The project is organized into the following key files and directories:

| File/Directory                | Purpose                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| `eduhub_mongodb_project.ipynb` | Primary project notebook detailing setup, data generation, CRUD, aggregation, and optimization. |
| `eduhub_queries.py`           | Production-ready Python file containing reusable CRUD and Aggregation functions. |
| `schema_validation.json`      | JSON document defining the schema validation rules applied to all collections. |
| `sample_data.json`            | JSON export containing sample data for all six collections.              |
| `performance_analysis.md`     | Document analyzing initial query performance, indexing strategy, and optimized results. |
| `docs/presentation.pptx`      | Final project summary and analysis.                                      |

## ▶️ Getting Started

To run this project, you must have MongoDB installed locally and accessible on the default port.

### Prerequisites
- **MongoDB**: Ensure your MongoDB server is running on `mongodb://localhost:27017/`.
- **Python**: Python 3.x installed.
- **Dependencies**: Install the required Python packages:
  ```bash
  pip install pymongo jupyter

FastAPI Product Management API
Overview

This is a FastAPI project for managing products using MySQL as the database. The API supports CRUD operations including listing, retrieving, adding, and updating products.
Features

List Products with pagination (/product/list)

Retrieve Product Info by ID (/product/{pid}/info)

Add New Product (/product/add)

Update Existing Product (/product/{pid}/update)

Uses SQLAlchemy ORM for database interactions

Pydantic for data validation

Error handling with transactions

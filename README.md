# Delivr Backend

FastAPI Backend Codebase for Delivr

## Setup

### Clone using Git

```sh
git clone https://github.com/delivr-tech/backend.git
cd backend
```

### Setup Workspace

This project uses a special `scripts/` environment powered by `dev.sh` to manage and run the environment.

```sh
# required to use any dev.sh commands
# (always run this in a new terminal session)
source dev.sh

# (set up once)
dev setup

# shows all available commands
dev help
```

### Run the Project

```sh
# run tests
dev test

# run application
dev run
```

## Architecture

The project follows a modular MRS (Models-Routes-Services) architecture, which is a common design pattern for modern FastAPI applications. This repository contains a slightly modified version of the typical MRS architecture.

### Module Overview

The main codebase is divided into a few modules:

- `core`: Contains the main application and configurations.
- `models`: Contains the data models and schemas.
- `routes`: Contains the API routes and endpoints.
- `services`: Contains the business logic and services
- `repo`: Contains the data access layer and repository classes.
- `utils`: Contains utility functions and helpers.

### API Design

The codebase follows a RESTful API design, with endpoints organized under the `/api/v1/` prefix. Each module has its own set of routes and services, making it easy to maintain and extend the application.

### Database Design

The database design follows a relational model, with tables representing the core entities of the application. Each table has a clear schema and relationships defined to ensure data integrity and consistency.

## Functionality

This backend provides the following functionalities:

- User authentication and authorization
- Personas:
  - Customer
    - create orders
    - view order history
    - manage profile
  - Seller
    - manage products
    - view sales history
    - manage profile
  - Admin
    - manage users
    - manage products
    - view sales history
    - view analytics
  - Delivery Agent
    - view assigned orders
    - update order status
    - manage profile
- CRON Jobs:
  - Delivery Route and Inventory Assignment
    - 8 AM Shift (Runs 7 AM, Daily)
    - 4 PM Shift (Runs 3 PM, Daily)


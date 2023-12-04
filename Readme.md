# Celes Technical Assessment API

## Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables: Create a `.env` file with necessary configurations.
   - FIREBASE_CREDS_URL: path to the Firebase Creds
   - DATA_PATH: path to the parket files folder
   - DATABASE_URL: url to the db
3. Run the application: `flask run`
4. Access the API at `http://localhost:5000/`

## Running it using docker:

1. Build the Docker image `docker build -t celes-client-api .`
2. Run the Docker container `docker run -p 5000:5000 --env-file .env celes-client-api`
   
## Testing

Run tests using pytest:

```bash
pytest tests
```

# Docs
Defined API Docs using Swagger available in the docs folder

## Celes API
Celes technical assessment documentation

## Version: 1.0

### /

#### GET
##### Summary:

Get mock response from root

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |

### /login

#### POST
##### Summary:

Another endpoint

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes | object |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful login |
| 401 | Unauthorized access |

### /getSalesByEmployee

#### GET
##### Summary:

Get sales by employee

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| employee_id | query | Employee ID | Yes | integer |
| start_date | query | Start date (YYYY-MM-DD) | Yes | string |
| end_date | query | End date (YYYY-MM-DD) | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |

### /getSalesByStore

#### GET
##### Summary:

Get sales by store

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| store_id | query | store ID | Yes | integer |
| start_date | query | Start date (YYYY-MM-DD) | Yes | string |
| end_date | query | End date (YYYY-MM-DD) | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |

### /getSalesByProduct

#### GET
##### Summary:

Get sales by product

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| product_id | query | product ID | Yes | integer |
| start_date | query | Start date (YYYY-MM-DD) | Yes | string |
| end_date | query | End date (YYYY-MM-DD) | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |

### /getSalesInformationByStore

#### GET
##### Summary:

Get sales information by a given store

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| store_id | query | Store ID | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |

### /getSalesInformationByProduct

#### GET
##### Summary:

Get sales information by a given product

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| product_id | query | product ID | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |

### /getSalesInformationByEmployee

#### GET
##### Summary:

Get sales information by a given employee

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| employee_id | query | employee ID | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 500 | Internal server error |
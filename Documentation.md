# GET KPI1

Return all KPI1 from db.

**URL** : `/api/kpi1`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : None

**Query Params**:

| Query Param              | Description                                                  | Type            |
|--------------------------|--------------------------------------------------------------|-----------------|
| service_id               | Identifier of traffic class.                                 | Optional[int]   |
| interval                 | 5-minute or 1-hour.                                          | Optional[str]   |
| interval_start_timestamp | Start time of the interval (Unix timestamp in milliseconds). | Optional[float] |
| interval_end_timestamp   | End time of the interval (Unix timestamp in milliseconds).   | Optional[float] |
| total_bytes              | Total number of bytes for the service.                       | Optional[int]   |


## Success Responses

**Condition** : No KPI1 exist.

**Code** : `200 OK`

**Content** : `{[]}`

### OR

**Condition** : One or more KPI1 exist.

**Code** : `200 OK`

**Content** : 

```json
[
    {
        "service_id": 1,
        "interval_start_timestamp": 1668885266920.0,
        "interval_end_timestamp": 1668885266915.0,
        "total_bytes": 8,
        "interval": "1-hour",
        "id": "9ba23ffd-87dd-4789-9303-a905a236bf0b"
    },
    {
        "service_id": 2,
        "interval_start_timestamp": 1768885266915.0,
        "interval_end_timestamp": 1768885266915.0,
        "total_bytes": 2,
        "interval": "5-minutes",
        "id": "c922c1e6-2639-4fb4-aa7e-68e3caad0a4d"
    }
]
```

## Error

**Condition** : Invalid query param given.

**Code** : `400 Bad Request`

**Content** : `"Invalid query params values, error: {'INVALID_QUERY_PARAM_NAME': [ERROR_MESSAGE]}"`

### OR

**Condition** : Something went wrong while trying to fetch the data.

**Code** : `500 Internal Error`

**Content** : `"Something went wrong. Try again later!"`


# GET KPI2

Return all KPI2 from db.

**URL** : `/api/kpi2`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : None

**Query Params**:

| Query Param              | Description                                                  | Type            |
|--------------------------|--------------------------------------------------------------|-----------------|
| cell_id                  | Cell ID of mobile user.                                      | Optional[UUID]  |
| interval                 | 5-minute or 1-hour.                                          | Optional[str]   |
| interval_start_timestamp | Start time of the interval (Unix timestamp in milliseconds). | Optional[float] |
| interval_end_timestamp   | End time of the interval (Unix timestamp in milliseconds).   | Optional[float] |
| number_of_unique_users   | Number of unique users for the cell.                         | Optional[int]   |


## Success Responses

**Condition** : No KPI2 exist.

**Code** : `200 OK`

**Content** : `{[]}`

### OR

**Condition** : One or more KPI2 exist.

**Code** : `200 OK`

**Content** : 

```json
[
    {
        "cell_id": "f7d18a9f-22ca-4a5c-87bc-e5a60eee01cc",
        "interval_start_timestamp": 1668885266920.0,
        "interval_end_timestamp": 1668885266915.0,
        "number_of_unique_users": 8,
        "interval": "1-hour"
    },
    {
        "cell_id": "0ab45a2d-2a2e-4f20-868c-4aeda9b60519",
        "interval_start_timestamp": 1768885266915.0,
        "interval_end_timestamp": 1768885266915.0,
        "number_of_unique_users": 12,
        "interval": "5-minute"
    }
]
```

## Error

**Condition** : Invalid query param given.

**Code** : `400 Bad Request`

**Content** : `"Invalid query params values, error: {'INVALID_QUERY_PARAM_NAME': [ERROR_MESSAGE]}"`

### OR

**Condition** : Something went wrong while trying to fetch the data.

**Code** : `500 Internal Error`

**Content** : `"Something went wrong. Try again later!"`
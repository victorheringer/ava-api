# Ava Api

Web scrapper and Api for Universidade Norte do Paraná teaching platform.

### `POST` **Timeline**

Returns json data about timeline.

- **URL**

```
/timeline
```

- **Data Params**

```json
{
  "login": "ava-login",
  "password": "ava-password",
  "reportId": 0,
  "semesterId": 0
}
```

- **Code** `200`

```json
[
  {
    "name": "string",
    "code": "number",
    "completeness": "number",
    "period": {
      "init": "dd/mm/yyyy",
      "final": "dd/mm/yyyy"
    },
    "grade": {
      "current": "number",
      "total": "number"
    }
  }
]
```

### `POST` **Courses**

Returns json data about a single user.

- **URL**

```
/courses
```

- **Data Params**

```json
{ "login": "ava-login", "password": "ava-password" }
```

- **Code** `200`

```json
[
  {
    "course": "string",
    "semesters": [
      {
        "semester": "string",
        "grade": {
          "status": "APROVADO | REPROVADO",
          "current": "number",
          "total": "number",
          "subjects": [
            { "current": "number", "total": "number" },
            { "current": "number", "total": "number" }
          ]
        },
        "ava": {
          "grade": {
            "current": "number",
            "total": "number"
          }
        },
        "activities": [
          {
            "name": "string",
            "code": "number",
            "completeness": "number",
            "period": {
              "init": "dd/mm/yyyy",
              "final": "dd/mm/yyyy"
            },
            "grade": {
              "current": "number",
              "total": "number"
            }
          }
        ]
      }
    ]
  }
]
```

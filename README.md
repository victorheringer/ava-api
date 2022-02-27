# Ava Api
![version](https://img.shields.io/badge/Version-0.0.1--beta-orange)

Web scrapper and api for Universidade Norte do Paraná teaching platform Colaborar-AVA.
This provides cohesive endpoints for accessing data from theirs system, since it
uses server side rendering allowing to create new tools!

**Projects built using ava-api:**

* [Ava Plus](https://github.com/danieltvaz/avaplus) - Mobile application for Ava.

## Setup

Since this api uses docker, just make sure to have it and docker-compose setup,
then copy the env file to setup your config:

```
cat ./src/.samble-env > ./src/.env 
```

Then, just run:

```
docker-compose up
```

## Endpoints

### **Courses**

<details>
<summary>POST /courses</summary>

**Returns a list of courses**

- **Request Body**

```json
{
  "login": "ava-login",
  "password": "ava-password",
}
```

- **Code** `200`

```json
[
  {
    "name": string,
    "semesters": [
      {
        "matriculation_id": string, 
        "semester_number": number, 
        "semester_name": string,
      },
    ]
  }
]
```
</details>

### **Semester**

<details>
<summary>POST /semesters/:matriculation_id</summary>

**Returns all activities in a semester**

- **Request Body**

```json
{
  "login": "ava-login",
  "password": "ava-password",
}
```

- **Code** `200`

```json
[
  {
    "name": string,
    "report_card_id?": string,
    "activities?": [
      {
        "name": string,
        "date": {
          "init": string,
          "end": string,
        }, 
      }
    ]
  }
]
      
```
</details>
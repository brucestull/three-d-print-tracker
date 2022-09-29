# 07 - Add Database Settings to Config Vars

## Resources:
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:

1. Save the database settings as Heroku "Config Vars" KEY-VALUE pairs similar to how we added the other "Config Vars":
    * Sample values, from earlier:
        ```
        Host        ec2-52-71-23-11.compute-1.amazonaws.com
        Database    d12en8ankbfql6
        User        fnsrzllkwjdrrf
        Port        5432
        Password    8c7ff88eb1c45aeccb61bf68d7540db7710e3c8adce41f8334b8f0f51aa534b4
        ```
    * Save the provided values as Heroku "Config Vars" using the following mapping:
        ```
        Host        -->>    DATABASE_HOST
        Database    -->>    DATABASE_NAME
        User        -->>    DATABASE_USER
        Port        -->>    DATABASE_PORT
        Password    -->>    DATABASE_PASSWORD
        ```
    * Sample "Config Vars":  
![08_config_vars_summary](https://user-images.githubusercontent.com/47562501/174795613-37bd5eba-6d47-4eec-b4b8-e0f673978c20.png)

1. Proceed to [Modify ALLOWED_HOSTS](08_modify_allowed_hosts.md)

## Repository Links:
[README.md](../README.md)
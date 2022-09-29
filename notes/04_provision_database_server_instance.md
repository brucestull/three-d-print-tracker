# 04 - Provision Database Server Instance

## Resources:
* [Heroku](https://www.heroku.com/)
* https://dashboard.heroku.com/

## Process:

1. Open dashboard for the application we created:  
![01_heroku_application_dashboard](https://user-images.githubusercontent.com/47562501/174793985-c1be51d6-88ca-4154-923a-f3f7acf2a6b4.png)

1. Click the "Configure Add-ons" links:  
![02_click_configure_add_ons](https://user-images.githubusercontent.com/47562501/174794334-bb31b7b3-3681-4d11-bfe6-ce8e9b030612.png)

1. Start search for "heroku postgres":  
![03_search_for_heroku_postgres](https://user-images.githubusercontent.com/47562501/174794371-33167ff3-4bf7-4e17-b551-857125a9f088.png)

1. Click "Heroku Postgres" item:  
![04_click_heroku_postgres_item](https://user-images.githubusercontent.com/47562501/174794404-cade8c58-62fe-408c-af7f-b9b90aa1f127.png)

1. Check order form and click "Submit Order Form" button:  
![05_check_order_form_and_click_submit_order_form_button](https://user-images.githubusercontent.com/47562501/174794435-75f3bddb-c4a0-431d-8398-bf77ee66db2a.png)

1. Click "Heroku Postgres" line item link:  
![06_select_heroku_postgres_line_item_link](https://user-images.githubusercontent.com/47562501/174794457-fff0a237-854c-401f-abca-7335f96385b8.png)

1. Select "Settings" tab:  
![07_select_settings_tab](https://user-images.githubusercontent.com/47562501/174794480-72e01b41-88b8-4e8d-90c3-394a73e9402b.png)

1. Click "View Credentials..." button:  
![08_click_view_credentials_button](https://user-images.githubusercontent.com/47562501/174794502-02ed043f-9281-4648-8d29-3a0977ff2494.png)

1. Take note of database server settings, we will need these values later:
    * Sample values:
        ```
        Host        ec2-52-71-23-11.compute-1.amazonaws.com
        Database    d12en8ankbfql6
        User        fnsrzllkwjdrrf
        Port        5432
        Password    8c7ff88eb1c45aeccb61bf68d7540db7710e3c8adce41f8334b8f0f51aa534b4
        ```  
![09_take_note_of_database_settings](https://user-images.githubusercontent.com/47562501/174794541-1e2ef6b2-f4c6-43db-8c4e-76dd7b3f6666.png)

1. Proceed to [Add DJANGO_SETTINGS_MODULE to Config Vars](05_add_django_settings_module_to_config_vars.md)


## Repository Links:
[README.md](../README.md)

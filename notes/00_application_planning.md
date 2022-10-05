# Application Planning

## Planning:

* Name:
    * `prints`

* Views:
    * List view of each model:
        * `ModelPrint`
        * `Filament`
        * `Manufacturer`

## User Flow for Create `ModelPrint`:
1. Function-based may be best option since we need to create a `FilamentInstance` just in time for the creation of `ModelPrint` instances.
    * Maybe use `form_valid()`?

## Ideas:
* How to delete and incorrectly entered `ModelPrint` instance and `FilamentInstance` instance?


## Repository Links:
* [Model Planning](./00_model_planning.md)
* [README.md](../README.md)
# Model Planning

## Planning:

* Model for the properties of individual prints (like a print of the letter 'A', or a print of 'Lower GI'):
    * Class Name:
        * `ModelPrint`
    * Attributes:
        * Primary:
            * `name`:
                * Examples:
                    * `Letter A`
                    * `Lower GI`
                    * `Letter B`
                    * `Dog`
            * `filament`:
                * ForeignKey of `Filament`.
        * Secondary:
            * `mass` or `weight`:
            * `public`
            * `filament_length_consumed`
            * `filament_mass_consumed`
            * `notes`
            * `future_work`
            * `print_troubles`

* Filament:
    * Class Name:
        * `Filament`
    * Attributes:
        * `material`:
            * Type of plastic: `PLA`, `PLA+`, `PET`, etc.
            * Possibly use `choices` here?
        * `manufacturer`:
            * ForeignKey of `Manufacturer`.
        * `diameter`

* Model for filamant manufacturer:
    * Class Name:
        * `Manufacturer`
    * Attributes:
        * `name`:
            * Name of the filament manufacturer.
        * OTHER_ATTRIBUTES


## Repository Links:
* [Application Planning](./00_application_planning.md)
* [README.md](../README.md)
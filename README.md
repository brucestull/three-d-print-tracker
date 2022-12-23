# Flynnt Knapp's Print Tracker

* NOTE: Author is using PowerShell for this guide.

## Resources

* [`router.register` - `basename`](https://www.django-rest-framework.org/api-guide/routers/#usage)
  * `basename`
    * The base to use for the URL names that are created. If unset the basename will be automatically generated based on the queryset attribute of the viewset, if it has one. Note that if the viewset does not include a queryset attribute then you must set basename when registering the viewset.

## Notes

* **TODO**: Need to check [Deployment checklist - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
* [Project Directory Structure](notes/00_directory_structure.md)

## Setup Process

1. [Setup Process](./notes_setup/README.md)

## Build the Application

1. [Build Print Tracker Application](./notes/README.md)

## Project State at Commits

* [`ModelPrintFormView`, `ModelPrintCreateView`, and `model_print_create_function` views example comparison - includes print statements](https://github.com/brucestull/see-3d/tree/df16b65892b0c7100eb11763e5b964297ee3a42d)

## Excellent resources, this project wouldn't have been possible without these

* CustomUser method: [Django Best Practices: Custom User Model - Will Vincent - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* Docutils: [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)
* DEV and PROD settings: [Configuring Django Settings for Production - thinkster.io](https://thinkster.io/tutorials/configuring-django-settings-for-production)

## Links to this project's pages

* Repository: [Flynnt Knapp's Print Tracker](https://github.com/brucestull/see-3d)
* Production Deployment: <https://flynnt-knapp-print-tracker.herokuapp.com/>

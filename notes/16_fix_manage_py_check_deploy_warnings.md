# Fix `manage.py check --deploy` Warnings

## Resources:
* [Run manage.py check --deploy](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#run-manage-py-check-deploy)

## Current Status:
```
    WARNINGS:
    ?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
    ?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
    ?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
    ?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.

    System check identified 4 issues (0 silenced).
```

## Process:







1. Proceed to []()

## Repository Links:
* Back to [Convert `ModelPrint` `CreateView` to Function-Based View](./15_convert_create_view_to_function_based.md)
* [README.md](../README.md)
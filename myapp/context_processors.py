from django.conf import settings


def site_url(request):
    """Provide `SITE_URL` to templates.

    Uses `settings.SITE_URL` when set; otherwise attempts to build
    an absolute URL from the `request` object. Returns an empty
    string if neither is available.
    """
    site = getattr(settings, "SITE_URL", "") or ""
    site = site.rstrip("/")
    if not site and request is not None:
        try:
            site = request.build_absolute_uri("/").rstrip("/")
        except Exception:
            site = ""
    return {"SITE_URL": site}

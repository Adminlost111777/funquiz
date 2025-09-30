from django.http import HttpResponsePermanentRedirect

class HttpsRedirectMiddleware:
    """
    Redirects http://funquiz.org to https://funquiz.org
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check scheme and host
        if (
            not request.is_secure() and 
            request.get_host() == "funquiz.org"
        ):
            return HttpResponsePermanentRedirect("https://funquiz.org" + request.get_full_path())

        response = self.get_response(request)
        return response


from rest_framework.throttling import AnonRateThrottle


class PostRateThrottle(AnonRateThrottle):
    '''Custom throttle for post requests'''
    scope = 'post'
    
    def allow_request(self, request, view):
        if request.method != "POST":
            return True
        return super().allow_request(request, view)
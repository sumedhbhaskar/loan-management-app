"""
Custom permissions to check if the user is an admin user or not
"""

from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    """ check if user is is_superuser==True"""

    def has_permission(self, request, view):
        """
        Return `True` if user is superuser, `False` otherwise.
        """
        if request.user.is_superuser == True:
            return True

        return False

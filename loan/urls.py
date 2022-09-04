"""
Loan app url configurations:
/loan/loan-type -> register new loan type
/loan/loan-apply  -> register new loan application
/loan/loan-validate/<int:pk>  -> list/retrive loan application to validate the loan status 
static url pattern is also added for KYC document(aadhaar) to be uploaded, all the media files goes to MEDIA folder
"""


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from .views import LoanApplicationViewsets, LoanViewsets, LoanValidateViewsets
from django.urls import include

router = SimpleRouter()
router.register(r"loan-type",LoanViewsets)
router.register(r"loan-apply",LoanApplicationViewsets)
router.register(r"loan-validate",LoanValidateViewsets)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



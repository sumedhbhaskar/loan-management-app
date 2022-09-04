"""
Loan app models

Loan model->Loan type, loan description
Loan application -> user, loan, age, gender, kyc document(aadhaar), status, comments

"""

from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


class Loan(models.Model):
    """ Loan type and Loan description """

    loan_type = models.CharField(_("Loan type"),max_length=32)
    loan_description = models.TextField(_("Loan Description"))

    def __str__(self) -> str:
        return f"{self.loan_type}"


class LoanApplication(models.Model):
    """ Loan aaplication model """

    class LoanStatus(models.TextChoices):
        """ loan status, it can be approved, pending and declined. Default is pending """
        APPROVED = 'AP', _('Approved')
        PENDING = 'PE', _('Pending')
        DECLINED = 'DE', _('Declined')
    

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Applicant")
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(_("Age"))
    gender = models.CharField(_("Gender"),max_length=6)
    address = models.TextField(_("Address"))
    aadhaar = models.ImageField(_("Aadhaar photo"))
    status = models.CharField(
        max_length=2,
        choices=LoanStatus.choices,
        default=LoanStatus.PENDING
    )
    comments = models.TextField(_("Comments on loan status"))

    def __str__(self) -> str:
        """ string on return of loan application object """
        return f"{self.user}, Loan type: {self.loan}, Status: {self.status}"

    




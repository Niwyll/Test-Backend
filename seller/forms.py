from django.forms import Form, UUIDField, TextInput, ValidationError
from seller.models import Order

class OrderSearchForm(Form):
    uuid = UUIDField(
        label="Order UUID",
        required=True,
        widget=TextInput(attrs={"placeholder": "Enter Order UUID", "class": "form-control"})
    )
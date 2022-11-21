import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 number."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 number."
        )


# class UppercaseValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[A-Z]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 uppercase letter."),
#                 code='password_no_upper',
#             )

#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 uppercase letter."
#         )


# class LowercaseValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[a-z]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 lowercase letter."),
#                 code='password_no_lower',
#             )

#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 lowercase letter."
#         )


# class SymbolValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 symbol: " +
#                   "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
#                 code='password_no_symbol',
#             )

#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 symbol: " +
#             "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
#         )
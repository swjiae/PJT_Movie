from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)

        # 추가 저장 필드: nickname, profile_image
        nickname = data.get("nickname")
        profile_img = data.get("profile_img")

        if nickname:
            user.nickname = nickname

        if profile_img:
            user.profile_img = profile_img

        user.save()
        return user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 간접 참조
        # get_user_model() : 현재 활성화된 유저 모델 클래스를 가지고 오는 함수
        model = get_user_model()

class CustomuserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 따로 선언하지 않으면 fields는 UserChangeForm에 있는 모든 fields를 사용하게 된다.
            # fields = '__all__'
            # 유저 관련 모든 데이터를 수정할 수 있기 때문에 보안에 위험
            # 그래서 유저들이 접근 가능한 필드들을 제한해야 한다.
        # fields를 선언하면 AbstractForm내에 있는 fields들에서 선택하면 된다.
        fields = ('email', 'first_name', 'last_name',)
from django.shortcuts import render
from rest_framework.views import APIView

# Main이라는 새로운 기능을 만들었는데 APIView 기능을 한다.
class Main(APIView):            # APIView : 서버-클라이언트가 데이터를 주고 받을 수 있도록 도와주는 역할
    def get(self, request):     # Main클래스를 get으로 실행했을 때
        return render(request, 'instapjt/main.html')
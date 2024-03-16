# 문자열 자르기
echo '1234567890' | awk -F " " '{ print substr($1, 3, 2) }'

# BCI-System
'사용자 감정이입을 위한 BCI 기반 뉴로로보틱스 시스템' 개발 코드

필요 패키지(need 'pip install')
python-dispatcher
websocket-client

흐름:
sub_data를 실행하면 웹 소켓 스트림이 생성됨,
cortex에서 handle_stream_data의 fac 부분에서 데이터를 핸들링할 수 있음,
분류된 감정에 따라 NAO의 애니메이션을 실행시키도록 함

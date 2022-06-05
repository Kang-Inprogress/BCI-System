# BCI-System
'사용자 감정이입을 위한 BCI 기반 뉴로로보틱스 시스템' 개발 코드

필요 패키지(need 'pip install') :
python-dispatch | websocket-client

실행에 필요한 작업:
python2.7버전이 python2 명령어로 실행될 수 있도록 설정해주는 것이 필요함.
(참고: https://passing-story.tistory.com/185)


흐름:
sub_data를 실행하면 웹 소켓 스트림이 생성됨,
cortex에서 handle_stream_data의 fac 부분에서 데이터를 핸들링할 수 있음,
분류된 감정에 따라 NAO의 애니메이션을 실행시키도록 함(python 3.7이상에서 정상작동함. 테스트 환경 3.9.12, 2.7.13)

기본적으로 오프라인 NAO가 아닌 로컬의 머신으로 향해 있음(IP: 127.0.0.1, Port: 9559)

LED 작동 부분을 주석처리해서 임시로 제거했으므로 실제 NAO는 주석을 제거해주고 실행하면 LED도 같이 실행됨
(anger_low, anger_high 부분만 해당)



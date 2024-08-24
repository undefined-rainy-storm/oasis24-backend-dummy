# Oasis24 Backend (dummy)

프론트엔드 작성에 사용되는 더미 백엔드 서버입니다.  

프론트엔드와의 값 교환 대상 중 우선 구현 사항어서, 프론트엔드에서 개발을 수행하기 위해 선정의된 내용을 담고 있습니다.  

## 시작하기

### 요구사항 설치
이 리포지토리는 Poetry 패키지 관리자로 관리되고 있습니다. Poetry 패키지 관리자를 설치하고 사용하시기 바랍니다.  
- Poetry: [Install Documentation](https://python-poetry.org/docs/)

### Poetry 환경에 의존성 설치
```sh
poetry install
```

### 서버 실행
```sh
poetry run flask run
```

### 테스트 실행
> [!NOTE]  
> 이 구현체는 테스트 코드가 정의되지 않았습니다.  

```sh
poetry run pytest
```

### 자동 생성된 API 문서
서버를 실행한 후 http://localhost:5000/apidocs 에 접속하여 확인하십시오.

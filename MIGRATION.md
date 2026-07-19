# 기존 8개 Chapter 저장소 통합 안내

현재 공개 저장소의 입문용 `chapter01`~`chapter08`은 부트캠프 자료로 보존하고, 이 패키지를 정규학기 트랙으로 병합하는 방식을 권장합니다.

## 안전한 통합안

1. 새 브랜치 `course/15-week`를 만듭니다.
2. 기존 `chapter01`~`chapter08`은 그대로 둡니다.
3. 이 패키지의 `course/`, `weeks/`, `datasets/`, `projects/`, `rubrics/`, `templates/`, `instructor/`, `scripts/`, `.github/`를 추가합니다.
4. 기존 `README.md`를 바로 덮어쓰지 말고 새 README와 비교해 15주 트랙 링크를 추가합니다.
5. 자동 검증이 통과한 뒤 Pull Request로 병합합니다.

## 권장 최종 구조

```text
├── bootcamp/ 또는 chapter01~chapter08/  # 기존 입문 자료
├── weeks/week01~week15/                 # 정규학기 자료
├── course/                              # 정규학기 운영 계획
└── README.md                            # 두 트랙 진입점
```

GitHub에 직접 반영하기 전 기존 링크와 LMS 공지를 확인하세요. 이 패키지는 기존 파일을 삭제하거나 원격 저장소를 변경하지 않습니다.

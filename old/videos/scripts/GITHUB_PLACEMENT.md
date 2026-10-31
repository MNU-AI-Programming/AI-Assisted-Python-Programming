# GitHub에 배치할 때 권장 구조

현재 GitHub 쓰기 권한이 차단되어 저장소에는 자동 업로드하지 못했습니다.

각 주차에 아래 `video-production` 폴더를 추가하는 방식을 권장합니다.

```text
weeks/week01/
├── README.md
├── slides.md
├── practice.ipynb
├── assignment.md
├── quiz.md
└── video-production/
    ├── lecture_script.md
    ├── recording_notes.md
    ├── recording_checklist.md
    ├── subtitle_draft.srt
    ├── lms_description.md
    └── thumbnail_text.md
```

이 패키지의 `weekXX` 폴더 안 파일을 해당 주차의 `video-production/` 아래에 복사하면 됩니다.

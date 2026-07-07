# Colab 링크 설정 안내

이 저장소의 각 Chapter에는 Google Colab 실행 버튼이 포함되어 있습니다.

초기 상태에서는 링크에 `niko2204`라는 자리표시자가 들어 있습니다.

예:

```text
https://colab.research.google.com/github/niko2204/AI-Programming-with-GenAI/blob/main/chapter01/practice.ipynb
```

GitHub에 업로드한 후 `niko2204`를 교수자 GitHub 아이디로 바꾸면 됩니다.

## 자동 변경 방법

터미널에서 다음 명령을 실행합니다.

```bash
python tools/update_colab_links.py YOUR_niko2204
```

예:

```bash
python tools/update_colab_links.py youngholee
```

저장소 이름이 다르면 `--repo` 옵션을 사용합니다.

```bash
python tools/update_colab_links.py youngholee --repo my-ai-coding-class
```

## 학생 안내

학생은 각 Chapter의 `Open in Colab` 버튼을 클릭한 뒤 다음 순서로 저장합니다.

1. `파일`
2. `드라이브에 사본 저장`
3. 자신의 Google Drive에 저장
4. 실습 수행
5. Colab 공유 링크 제출

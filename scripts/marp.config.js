// Marp CLI 설정: 이모지를 시스템 글꼴로 그려 오프라인에서도 PDF가 깨지지 않게 한다.
module.exports = {
  allowLocalFiles: true,
  options: { emoji: { shortcode: false, unicode: false } },
};

function onOpen() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const today = new Date();
  
  // 1. 현재 날짜의 주차(Week) 계산 (예: "23주차" 또는 "W23")
  const weekName = getWeekNumberString(today); 
  
  // 2. 해당 주차 시트 열기
  const sheet = ss.getSheetByName(weekName);
  
  if (sheet) {
    ss.setActiveSheet(sheet);
    
    // 3. 오늘 날짜 셀에 조건부 서식(색상 변경) 적용
    applyTodayHighlight(sheet, today);
  } else {
    Logger.log("해당 주차의 시트를 찾을 수 없습니다: " + weekName);
  }
}

/**
 * 현재 날짜가 올해의 몇 번째 주차인지 계산하여 시트 이름 형식을 반환합니다.
 * 시트 이름이 "23주차" 형태라고 가정합니다. (필요시 수정 가능)
 */
function getWeekNumberString(date) {
  const baseDate = new Date(2026, 2, 16); // 2026-03-19 이거 시작 주차를 구하는거라 하나씩 밀릴수 있으니 1주차에 구성된 월요일 3.16 자바로는 2.16을 설정해야 정확하게 계산됨

  const diffTime = date.getTime() - baseDate.getTime();
  const diffDays = Math.floor(diffTime / 86400000);

  const weekNum = Math.floor(diffDays / 7) + 1;

  return weekNum + "주";
}
/*
function getWeekNumberString(date) {
  // 1주차가 시작된 임의의 기준일을 적어줍니다. (예: 2026년 3월 16일 월요일)
  // ※ 주의: 자바스크립트에서 월(Month)은 0부터 시작하므로 3월은 '2'로 적어야 합니다.
  const baseDate = new Date(2026, 2, 19); 
  
  // 기준일과 오늘 날짜의 차이 계산
  const diffInMs = date - baseDate;
  const diffInDays = Math.floor(diffInMs / (1000 * 60 * 60 * 24));
  
  // 7일로 나누어 주차 계산 (소수점 올림)
  let weekNum = Math.ceil((diffInDays + 1) / 7);
  
  // 만약 기준일보다 이전이라 음수가 나오면 1주로 고정
  if (weekNum < 1) weekNum = 1;
  
  return weekNum + "주";
}
*/
/**
 * 시트 전체에서 오늘 날짜를 찾아 배경색을 변경하는 조건부 서식을 적용합니다.
 */
function applyTodayHighlight(sheet, today) {
  // 기존의 모든 조건부 서식 규칙을 가져옴
  const rules = sheet.getConditionalFormatRules();
  
  // 동일한 '오늘 날짜' 규칙이 중복 쌓이지 않도록 기존 규칙을 유지하되, 새로 정의할 수도 있습니다.
  // 여기서는 스크립트 실행 시마다 깔끔하게 적용하기 위해 사용자 정의 수식 규칙을 추가합니다.
  
  // 데이터가 있는 전체 범위 지정
  const lastRow = sheet.getLastRow() || 1;
  const lastColumn = sheet.getLastColumn() || 1;
  const range = sheet.getRange(1, 1, lastRow, lastColumn);
  
  // 구글 스프레드시트 수식으로 '오늘'과 일치하는지 확인하는 조건부 서식 생성
  const rule = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied('=A1=TODAY()') // 데이터 범위의 시작점(A1)을 기준으로 오늘 날짜 비교
    .setBackground('#FFE082') // 강조할 배경색 (연한 주황/노란색 예시)
    .setFontColor('#000000')   // 글자색 (검은색)
    .setRanges([range])
    .build();
  
  // 기존 규칙 리스트에 추가 후 시트에 반영
  rules.push(rule);
  sheet.setConditionalFormatRules(rules);
}
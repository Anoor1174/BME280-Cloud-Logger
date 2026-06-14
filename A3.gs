var SHEET_NAME = "A3";
var COUNTER_CELL = "F2";

function doGet(e) {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet();
  var SHEET = spreadSheet.getSheetByName(SHEET_NAME);
  var lastLog = SHEET.getRange(COUNTER_CELL).getValue();
  if (!lastLog || lastLog < 1) {
    lastLog = 2;  
  } else {
    lastLog = lastLog + 1;
  }
  SHEET.getRange(COUNTER_CELL).setValue(lastLog);

  SHEET.getRange("A" + lastLog).setValue(e.parameter.time);
  SHEET.getRange("B" + lastLog).setValue(e.parameter.temp);
  SHEET.getRange("C" + lastLog).setValue(e.parameter.press);
  SHEET.getRange("D" + lastLog).setValue(e.parameter.hum);

  return ContentService.createTextOutput("Data Received at row " + lastLog);
}
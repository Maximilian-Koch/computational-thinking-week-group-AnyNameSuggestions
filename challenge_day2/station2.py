from datetime import datetime
 # Mapping of English weekday names to Japanese
english_to_japanese = {
    'Monday': '月曜日',
    'Tuesday': '火曜日',
    'Wednesday': '水曜日',
    'Thursday': '木曜日',
    'Friday': '金曜日',
    'Saturday': '土曜日',
    'Sunday': '日曜日'
}

def solution_station_2(date_str : str) -> str:
    # Parse the input string to a date object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the weekday name
    weekday_name = date_obj.strftime('%A')
    
    return english_to_japanese[weekday_name]
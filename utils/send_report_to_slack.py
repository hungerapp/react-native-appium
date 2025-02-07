import os
import requests
import json
from datetime import datetime

def format_duration(seconds):
    """
    change seconds to minutes and seconds
    """
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f"{minutes}分{remaining_seconds}秒"

def send_report_to_slack(webhook_url, allure_report_path, message=None):
    """
    Send Allure report to Slack
    """
    try:
        # slack config -> kindly remind don't put your own token here
        SLACK_BOT_TOKEN = "xoxb-857694753079-8386879001525-QUmI7GE14VL5NxQevi6apGMC"
        SLACK_CHANNEL = "C08B92NPHF0"  # your channel id
        
  
        if message:
            slack_message = message
        else:
            summary_json_path = os.path.join(allure_report_path, 'widgets', 'summary.json')
            print(f"正在讀取報告文件: {summary_json_path}")
            
            if not os.path.exists(summary_json_path):
                print(f"找不到報告文件: {summary_json_path}")
                return
                
            with open(summary_json_path, 'r') as f:
                summary_content = f.read()
                print(f"報告內容: {summary_content}")
                summary = json.loads(summary_content)
            
         
            statistic = summary.get('statistic', {})
            total = statistic.get('total', 0)
            passed = statistic.get('passed', 0)
            failed = statistic.get('failed', 0)
            skipped = statistic.get('skipped', 0)
            
            # 獲取執行時間
            time_data = summary.get('time', {})
            duration_ms = time_data.get('duration', 0)
            duration_min = int((duration_ms / 1000) // 60)
            duration_sec = int((duration_ms / 1000) % 60)
            
            # 建構訊息
            slack_message = {
                "text": "自動化測試報告 🤖",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*自動化測試報告 🤖*\n執行時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": (
                                    f"*測試結果:*\n"
                                    f"總數: {total}\n"
                                    f"通過: {passed} ✅\n"
                                    f"失敗: {failed} ❌\n"
                                    f"跳過（開發中）: {skipped} ⏭️\n"
                                    f"執行時間: {duration_min}分{duration_sec}秒 ⏱️"
                                )
                            }
                        ]
                    }
                ]
            }
            
            # 印出讀取到的數據以便除錯
            print(f"讀取到的測試結果：")
            print(f"總數: {total}")
            print(f"通過: {passed}")
            print(f"失敗: {failed}")
            print(f"跳過: {skipped}")
            print(f"執行時間: {duration_min}分{duration_sec}秒")
        
        # send to slack
        print(f"正在發送消息到 Slack: {json.dumps(slack_message, indent=2)}")
        response = requests.post(webhook_url, json=slack_message)
        response.raise_for_status()
        print(f"Slack 響應狀態碼: {response.status_code}")
        
        video_path = None
        for root, dirs, files in os.walk('allure-results'):
            for file in files:
                if file.endswith('.mp4'):
                    video_path = os.path.join(root, file)
                    break
            if video_path:
                break
        
        if video_path:
            print(f"正在上傳視頻: {video_path}")
            
            headers = {
                'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
            }
            
            with open(video_path, 'rb') as video_file:
                files = {
                    'file': video_file,
                    'initial_comment': '測試錄影 📹',
                    'channels': SLACK_CHANNEL
                }
                
                upload_response = requests.post(
                    'https://slack.com/api/files.upload',
                    headers=headers,
                    files=files
                )
                
                if upload_response.status_code == 200 and upload_response.json().get('ok'):
                    print("上傳成功 ✅")
                else:
                    print(f"上傳失敗: {upload_response.text} ❌")
        
        print("測試報告已成功發送到 Slack")
        
    except Exception as e:
        print(f"發送報告到 Slack 時發生錯誤: {str(e)}")
        import traceback
        print(traceback.format_exc())
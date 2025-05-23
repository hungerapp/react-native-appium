import json
import time
import requests
from datetime import datetime
import os
from typing import Dict, List, Optional

class LokiLogger:
    def __init__(self, loki_url: str):
        self.loki_url = loki_url
        self.project = "react-native-appium"
        self.env = os.getenv("ENV", "staging")

    def _get_timestamp(self) -> str:
        return str(int(time.time() * 1e9))

    def send_log(self,
                test_name: str,
                feature: str,
                scenario: str,
                status: str,
                duration: float,
                tags: List[str],
                platform: str,
                os_version: str,
                device_name: str,
                browserstack_session: Optional[str] = None,
                git_branch: Optional[str] = None,
                git_commit: Optional[str] = None,
                ci_job_id: Optional[str] = None,
                ci_pipeline: Optional[str] = None,
                report_url: Optional[str] = None,
                error_message: Optional[str] = None,
                stack_trace: Optional[str] = None,
                retry_attempt: Optional[int] = None) -> None:
        
        log_data = {
            "project": self.project,
            "type": "app",
            "test_name": test_name,
            "feature": feature,
            "scenario": scenario,
            "status": status,
            "duration": duration,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "env": self.env,
            "tags": tags,
            "platform": platform,
            "os_version": os_version,
            "device_name": device_name,
            "browserstack_session": browserstack_session,
            "git_branch": git_branch,
            "git_commit": git_commit,
            "ci_job_id": ci_job_id,
            "ci_pipeline": ci_pipeline,
            "report_url": report_url,
            "error_message": error_message,
            "stack_trace": stack_trace,
            "retry_attempt": retry_attempt
        }

        # 移除 None 值的欄位
        log_data = {k: v for k, v in log_data.items() if v is not None}

        # Loki 格式：labels 放在 stream，內容放在 values
        labels = {
            "project": self.project,
            "env": self.env,
            "type": "app",
            "test_name": test_name,
            "status": status,
            "platform": platform,
            "os_version": os_version,
            "device_name": device_name
        }
        # tags 也可以合併成一個 label 字串
        if tags:
            labels["tags"] = ",".join(tags)
        if git_branch:
            labels["git_branch"] = git_branch
        if ci_pipeline:
            labels["ci_pipeline"] = ci_pipeline

        loki_payload = {
            "streams": [
                {
                    "stream": labels,
                    "values": [
                        [self._get_timestamp(), json.dumps(log_data, ensure_ascii=False)]
                    ]
                }
            ]
        }

        try:
            response = requests.post(
                self.loki_url,
                json=loki_payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            print(f"Log sent successfully to Loki: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending log to Loki: {str(e)}")
            print(f"Payload: {json.dumps(loki_payload, indent=2)}")

# 創建全局實例
loki_logger = LokiLogger("http://198.19.249.147:3100/loki/api/v1/push") 
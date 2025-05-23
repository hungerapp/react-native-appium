from .loki_logger import loki_logger
import time

def example_test():
    start_time = time.time()
    
    try:
        # 模擬測試執行
        time.sleep(1)
        
        # 測試成功的情況
        duration = time.time() - start_time
        loki_logger.send_log(
            test_name="user can add item to cart",
            feature="Shopping Cart",
            scenario="Add Item to Cart",
            status="passed",
            duration=duration,
            tags=["@regression", "@cart"],
            platform="Android",
            os_version="14.0",
            device_name="Samsung Galaxy S23",
            browserstack_session="https://app-automate.browserstack.com/sessions/abcd1234efgh5678",
            git_branch="feature/cart",
            git_commit="f6e5d4c3",
            ci_job_id="app-ci-112233",
            ci_pipeline="GitLab CI",
            report_url="https://ci.example.com/reports/app/112233"
        )
        
    except Exception as e:
        # 測試失敗的情況
        duration = time.time() - start_time
        loki_logger.send_log(
            test_name="user can add item to cart",
            feature="Shopping Cart",
            scenario="Add Item to Cart",
            status="failed",
            duration=duration,
            tags=["@regression", "@cart"],
            platform="Android",
            os_version="14.0",
            device_name="Samsung Galaxy S23",
            browserstack_session="https://app-automate.browserstack.com/sessions/abcd1234efgh5678",
            git_branch="feature/cart",
            git_commit="f6e5d4c3",
            ci_job_id="app-ci-112233",
            ci_pipeline="GitLab CI",
            report_url="https://ci.example.com/reports/app/112233",
            error_message="Element not found: 'Add to Cart' button",
            stack_trace=str(e),
            retry_attempt=1
        )

if __name__ == "__main__":
    example_test() 